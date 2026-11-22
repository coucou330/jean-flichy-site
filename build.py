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
"""
from __future__ import annotations

import datetime as dt
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
OUT = ROOT / "docs"

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)


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
    env.globals.update(site=site, url=u)
    env.filters["entities"] = encode_entities

    def render_md(text: str) -> Markup:
        md.reset()
        return Markup(prefix_links(md.convert(COMMENT.sub("", text or ""))))

    env.filters["md"] = render_md

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
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    if site.get("cname"):
        (OUT / "CNAME").write_text(site["cname"].strip() + "\n", encoding="utf-8")

    for page in pages:
        page["content"] = render_md(page["body"])
        tpl = env.get_template(f"{page['layout']}.html")
        html = tpl.render(page=page, projects=projects, live_urls=live_urls)
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
