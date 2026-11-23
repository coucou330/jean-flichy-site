---
# Étape 3 : page courte (stub). Étude de cas complète à l'étape 5.
title: Airship weather operability
subtitle: When can a 200-metre cargo airship safely leave its hangar?
layout: project
order: 5
card_meta: Flying Whales
year: "2025"
card_summary: When can a 200-metre cargo airship leave its hangar?
filters: [Research]
dates: 23 June – 25 July 2025 (5 weeks)
where: Flying Whales, Operations – Engineering team
role: Operations data intern
tags: [Data, Weather, Transport]
tools: [Python]
description: Flying Whales internship — six months of on-site LiDAR wind data against AROME forecasts, turned into operability statistics and a go/no-go rule.
image: { base: /img/projects/airship-wind-rose, h: 500, max_w: 1220, alt: "Wind rose of six months of LiDAR measurements at 50 m, weighted by wind speed, with dominant south-easterly winds", caption: "Wind rose of the on-site LiDAR measurements at 50 m, weighted by wind speed so that strong winds stand out.", credit: "Figure: Jean Flichy, internship report" }
gallery_layout: wide
gallery:
  - { base: /img/projects/airship-lidar-vs-arome, h: 287, max_w: 945, alt: "Time series of wind speed at 50 m: LiDAR measurements and AROME six-hour forecasts over eight days of July 2025", caption: "LiDAR measurements against Météo-France AROME six-hour forecasts, July 2025.", credit: "Figure: Jean Flichy, internship report" }
  - { base: /img/projects/airship-hangar-angle, h: 447, max_w: 945, alt: "Line chart of the share of days with operations possible as a function of hangar orientation, peaking near 141 degrees", caption: "Share of days when an operation is possible, as a function of the hangar's orientation.", credit: "Figure: Jean Flichy, internship report" }
  - { base: /img/projects/airship-threshold, h: 410, max_w: 945, alt: "Accuracy, false negatives and false positives as a function of the forecast wind threshold, with an optimum at 17.6 m/s", caption: "Choosing the forecast threshold for a go/no-go rule: accuracy against missed opportunities and risky false positives.", credit: "Figure: Jean Flichy, internship report" }
---
<!-- src : rapport EDI (LCA60T 200 m ; LiDAR 50–300 m ; AROME ; 6 mois) ; année 2025 (coquille 2024 dans le rapport). -->

**TL;DR** — Flying Whales is developing the LCA60T, a 200-metre rigid airship for heavy cargo. I studied whether the weather at its future final assembly site would let it operate, compared six months of on-site LiDAR wind measurements with Météo-France AROME forecasts, and proposed a go/no-go framework that weighs safety against cost.

<p class="stub-note">Full write-up coming this week.</p>
