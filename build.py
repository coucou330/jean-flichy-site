#!/usr/bin/env python3
"""Build the static site: content/ (Markdown + YAML front matter) + templates/ + static/ -> docs/.

Usage:
    python build.py                 # build with base_url from site.yml (GitHub Pages)
    BASE_URL= python build.py       # build for the root of a domain (or local preview)
    python -m http.server -d docs   # preview locally (build with BASE_URL= first)

Rules:
- Files whose name starts with "_" (e.g. content/work/_template.md) are never built.
- Pages with `draft: true` in their front matter are not built and drop out of nav/lists.
- HTML comments in Markdown (<!-- ... -->) are internal notes: they are stripped before rendering.
- Every root-relative link ("/work/") gets the base_url prefix, so the site works both under
  /jean-flichy-site/ and at the root of a custom domain.
- data/*.yml files are loaded as `data.<name>` in templates (e.g. data/path.yml -> data.path).
- A paragraph that contains only [[include:NAME]] in Markdown is replaced by templates/partials/NAME.html;
  [[figure:KEY]] or [[figures:KEY1,KEY2]] inserts figures described in data/figures.yml.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
DATA = ROOT / "data"
OUT = ROOT / "docs"

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)
INCLUDE = re.compile(r"<p>\[\[(include|figures?):([a-z0-9_,-]+)\]\]</p>")


def load_site() -> dict:
    site = yaml.safe_load((ROOT / "site.yml").read_text(encoding="utf-8"))
    if "BASE_URL" in os.environ:
        site["base_url"] = os.environ["BASE_URL"]
    site["base_url"] = (site.get("base_url") or "").rstrip("/")
    site["year"] = dt.date.today().year
    site["built"] = dt.date.today().isoformat()
    return site


def read_page(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = FRONT_MATTER.match(text)
    meta, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, text)
    return meta, body


def url_for(path: Path) -> str:
    rel = path.relative_to(CONTENT).with_suffix("")
    parts = list(rel.parts)
    if parts[-1] == "index":
        parts = parts[:-1]
    if parts == ["404"]:
        return "/404.html"
    return "/" + "/".join(parts) + ("/" if parts else "")


def out_file(url: str) -> Path:
    if url.endswith(".html"):
        return OUT / url.lstrip("/")
    return OUT / url.lstrip("/") / "index.html"


def encode_entities(s: str) -> Markup:
    """Encode every character as a decimal HTML entity (light protection against e-mail scrapers)."""
    return Markup("".join(f"&#{ord(c)};" for c in s))


def minify_css(css: str) -> str:
    """Small, safe CSS minifier: drop comments and collapse whitespace (no reordering)."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    css = re.sub(r":\s+", ":", css)  # "a: b" -> "a:b" (selectors like "a :hover" are not used)
    css = css.replace(";}", "}")
    return css.strip() + "\n"


def main() -> None:
    site = load_site()
    base = site["base_url"]

    def u(path: str) -> str:
        """Prefix a root-relative URL with base_url; leave external links and anchors alone."""
        if not path or not path.startswith("/") or path.startswith("//"):
            return path
        return base + path

    def prefix_links(html: str) -> str:
        return re.sub(r'(href|src|srcset)="(/(?!/)[^"]*)"', lambda m: f'{m.group(1)}="{u(m.group(2))}"', html)

    md = markdown.Markdown(extensions=["extra", "sane_lists", "smarty"],
                           extension_configs={"smarty": {"smart_quotes": False}})

    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]),
                      trim_blocks=True, lstrip_blocks=True)
    data = {f.stem: yaml.safe_load(f.read_text(encoding="utf-8"))
            for f in sorted(DATA.glob("*.yml"))} if DATA.exists() else {}
    env.globals.update(site=site, url=u, data=data,
                       all_media=lambda items: all(i.get("image") or i.get("placeholder") for i in items))
    env.filters["entities"] = encode_entities

    # schema.org Person, printed as JSON-LD on the home page
    person = site.get("person") or {}
    abs_root = site["origin"].rstrip("/") + base + "/"
    person_ld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": site["author"]["name"],
        "url": abs_root,
        "image": site["origin"].rstrip("/") + u("/img/portrait-800.jpg"),
        "jobTitle": person.get("job_title"),
        "alumniOf": [{"@type": "CollegeOrUniversity", "name": n} for n in person.get("alumni_of", [])],
        "sameAs": [site["author"]["linkedin"]],
    }
    env.globals["person_jsonld"] = Markup(json.dumps({k: v for k, v in person_ld.items() if v},
                                                     ensure_ascii=False).replace("</", "<\\/"))

    def render_md(text: str) -> Markup:
        md.reset()
        html = prefix_links(md.convert(COMMENT.sub("", text or "")))
        # Partials build their own links with url(): include them after prefixing.
        def shortcode(m: re.Match) -> str:
            kind, arg = m.group(1), m.group(2)
            if kind == "include":
                return env.get_template(f"partials/{arg}.html").render()
            figs = [data["figures"][k] for k in arg.split(",")]
            return env.get_template("partials/figures.html").render(figs=figs)
        html = INCLUDE.sub(shortcode, html)
        return Markup(html)

    env.filters["md"] = render_md

    def inline_md(text: str) -> Markup:
        """Render a one-line Markdown string without the surrounding <p>."""
        html = str(render_md(text)).strip()
        if html.startswith("<p>") and html.endswith("</p>") and html.count("<p>") == 1:
            html = html[3:-4]
        return Markup(html)

    env.filters["inline_md"] = inline_md

    # Collect pages
    pages = []
    for path in sorted(CONTENT.rglob("*.md")):
        if any(part.startswith("_") for part in path.relative_to(CONTENT).parts):
            continue
        meta, body = read_page(path)
        if meta.get("draft") is True:
            continue
        pages.append({**meta, "url": url_for(path), "source": path, "body": body,
                      "layout": meta.get("layout", "page")})

    live_urls = {p["url"] for p in pages}
    site["nav"] = [n for n in site.get("nav", []) if n["url"] in live_urls]
    projects = sorted([p for p in pages if p["layout"] == "project"],
                      key=lambda p: p.get("order", 99))

    # Fresh output
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT)
    for css in OUT.rglob("*.css"):
        css.write_text(minify_css(css.read_text(encoding="utf-8")), encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    if site.get("cname"):
        (OUT / "CNAME").write_text(site["cname"].strip() + "\n", encoding="utf-8")

    for page in pages:
        page["content"] = render_md(page["body"])
        tpl = env.get_template(f"{page['layout']}.html")
        html = COMMENT.sub("", tpl.render(page=page, projects=projects, live_urls=live_urls))
        target = out_file(page["url"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print(f"  {page['url']:<40} <- {page['source'].relative_to(ROOT)}")

    # sitemap.xml + robots.txt
    abs_base = site["origin"].rstrip("/") + base
    locs = "\n".join(f"  <url><loc>{abs_base}{p['url']}</loc><lastmod>{site['built']}</lastmod></url>"
                     for p in pages if p["url"] != "/404.html")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + locs + "\n</urlset>\n",
        encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {abs_base}/sitemap.xml\n",
                                    encoding="utf-8")
    print(f"Built {len(pages)} pages into {OUT.relative_to(ROOT)}/ (base_url='{base}')")


if __name__ == "__main__":
    main()
