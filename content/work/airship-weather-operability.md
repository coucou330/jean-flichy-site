---
# Étape 5 (25/11) : étude de cas complète (brouillon + rapport EDI ; faits ✅ INVENTAIRE B et H). Graphiques extraits le 23/11 (aucune image de l'entreprise).
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
tools: [Python, Jupyter, Météo-France data, ROC / confusion-matrix analysis]
description: Flying Whales internship — six months of on-site LiDAR wind data against AROME forecasts, turned into operability statistics and a go/no-go rule.
image: { base: /img/projects/airship-wind-rose, h: 500, max_w: 1220, alt: "Wind rose of six months of LiDAR measurements at 50 m, weighted by wind speed, with dominant south-easterly winds", caption: "Wind rose of the on-site LiDAR measurements at 50 m, weighted by wind speed so that strong winds stand out.", credit: "Figure: Jean Flichy, internship report" }
gallery_layout: wide
gallery:
  - { base: /img/projects/airship-lidar-vs-arome, h: 287, max_w: 945, alt: "Time series of wind speed at 50 m: LiDAR measurements and AROME six-hour forecasts over eight days of July 2025", caption: "LiDAR measurements against Météo-France AROME six-hour forecasts, July 2025.", credit: "Figure: Jean Flichy, internship report" }
  - { base: /img/projects/airship-hangar-angle, h: 447, max_w: 945, alt: "Line chart of the share of days with operations possible as a function of hangar orientation, peaking near 141 degrees", caption: "Share of days when an operation is possible, as a function of the hangar's orientation.", credit: "Figure: Jean Flichy, internship report" }
  - { base: /img/projects/airship-threshold, h: 410, max_w: 945, alt: "Accuracy, false negatives and false positives as a function of the forecast wind threshold, with an optimum at 17.6 m/s", caption: "Choosing the forecast threshold for a go/no-go rule: accuracy against missed opportunities and risky false positives.", credit: "Figure: Jean Flichy, internship report" }
---
<!-- src générale : Google Doc « EDI internship report » (1eoY21CSmZOE2UhDwyaXvB2JthS77JhVmUJEDJXP0xXE) ; CV ETH ; INVENTAIRE B et H. Année 2025 (coquille 2024 dans le rapport). « pandas » non confirmé → non cité. Encadrant non nommé. -->

**TL;DR** — Flying Whales is developing the LCA60T, a 200-metre rigid airship for heavy cargo. I studied whether the weather at its future final assembly site would let it operate, compared six months of on-site LiDAR wind measurements with Météo-France AROME forecasts, and proposed a go/no-go framework that weighs safety against cost.

## Context

The LCA60T is designed to carry up to 60 tonnes. An airship that size cannot leave its hangar in strong or badly aligned wind. The company needed two answers for its final assembly site at Laruscade, in Gironde: how often operations will be possible — to plan the test phase and price the service — and how to decide, day by day, using forecasts that are never perfect.
<!-- src : rapport EDI (LCA60T 200 m, 60 t, Laruscade, fiche d'objectifs) -->

## What I did

- **Audited the data.** The on-site LiDAR measures the wind every 4 seconds, every 20 m from 50 to 300 m. About 7% of the values over the period were missing or invalid. I linked the gaps to low temperatures and noise and, with the team, to the probable effect of a nearby building's orientation.
- **Described the site's wind.** I built configurable wind roses, checked the day–night wind cycle across France on about 100 weather stations over ten years, and plotted the "dangerous cases": conditions that could damage the airship outside occurred in about 0.01% of cases over six months.
- **Coded the operating rules** for three operations — leaving the hangar, take-off and landing, and load exchange — with their time windows, and computed how many days each would be possible.
- **Tested the forecasts.** I resampled the 4-second measurements to compare them with AROME's hourly forecasts, then scored the forecast as a classifier, with ROC curves and confusion matrices.
<!-- src : rapport EDI (4 s, 20 m, 50–300 m, ~7 %, 100 stations, 10 ans, 0,01 %, 3 opérations, ROC) -->

## Results

- AROME slightly **over-predicts** wind speed — the safe side — but its errors can reach about 3 m/s in speed and 60° in direction.
- As a classifier, the forecast is good: the area under the ROC curve is above 0.8 for every variable.
- For a sample mission — a two-hour round trip with a one-hour load exchange — forecasts and observations agreed in 64% of cases; 20% were missed opportunities and 3% were risky false positives.
- **Hangar orientation** turned out to drive the number of operable days. It was already fixed at Laruscade, but the method can help choose the orientation of future bases.
- A **go/no-go rule** that tunes the forecast threshold to balance the cost of a missed day against the risk of a failed mission.
- Deliverables: a 50-page report, the analysis notebooks, and a tool that maps every Météo-France station and plots its wind rose over any period. I presented the results to the team.
<!-- src : rapport EDI (3 m/s, 60°, AUC > 0,8, 64/20/3 %, 50 pages, carte des stations) -->

**One limit.** The routine that downloaded the forecasts first pointed at the wrong coordinates. It was fixed, but only four weeks of forecasts could be compared with the measurements, so the figures should be confirmed over a longer period.
<!-- src : rapport EDI (routine AWS sur de mauvaises coordonnées, corrigée ; 4 semaines) — INVENTAIRE H : « limite, à citer avec prudence » -->

## What I learned

Real data is messy, and most of the work is deciding what you can trust. I also learned that a forecast is only as useful as the decision rule built on top of it. The same question comes up in energy systems, for grids and wind farms, and it is part of what drew me there.
<!-- src : rapport EDI (conclusion) ; lien vers l'énergie : lettre ETH -->
