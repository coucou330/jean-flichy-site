---
# Étape 3 : page courte (stub). Étude de cas complète à l'étape 4 (brouillon : 02 Contenu/brouillons/quebec-grid-resilience.md).
title: Québec grid resilience
subtitle: How far can an extreme winter push Québec's transmission grid before load must be shed?
layout: project
order: 1
card_meta: Capstone, McGill
year: 2026–27
card_summary: How far can an extreme winter push Québec's grid before load must be shed?
filters: [Energy, Research]
dates: September 2026 – April 2027 (in progress)
where: McGill University, Montréal — ECSE 458 Capstone Design Project
team: Four students
role: Grid modelling and AC power flow
supervisor: Prof. Xiaozhe Wang
tags: [Energy, Power systems, Modelling]
tools: [PyPSA, pandapower, Python]
description: Capstone project — an open model of Hydro-Québec's grid, extended to 315 kV and made to converge in AC power flow, to study cascading failures in ice and wind storms.
image: { base: /img/projects/capstone-peak-voltages, h: 500, max_w: 1600, alt: "Map of the Québec 735 kV and 315 kV network model, buses coloured by voltage at the January 2022 peak hour", caption: "Our corrected model at the peak hour of the test week (3 January 2022, 17:00): every bus voltage, 735 kV and 315 kV lines.", credit: "Figure: capstone team" }
gallery_layout: wide
gallery:
  - { base: /img/projects/capstone-line-lengths, h: 294, max_w: 1600, alt: "Scatter plot showing stored line lengths about 1.4 to 1.7 times too long as latitude increases, and a bar chart comparing 735 kV kilometres in the model with Hydro-Québec's inventory", caption: "Why the AC model diverged: line lengths had been measured in Web Mercator, which stretches them by 1/cos(latitude) — 41 % to 66 % too long.", credit: "Figure: capstone team" }
  - { base: /img/projects/capstone-test-week, h: 378, max_w: 1600, alt: "Hourly demand of the January 2022 test week above the band of bus voltages in the model", caption: "The test week, 1–7 January 2022: Hydro-Québec demand (top) and the range of bus voltages in the model at every hour (bottom).", credit: "Figure: capstone team" }
  - { base: /img/projects/capstone-load-margin, h: 347, max_w: 1600, alt: "P-V curves of the lowest bus voltage as load and generation are scaled up at the peak hour", caption: "Load margin at the peak hour: voltage, not line ratings, sets the limit.", credit: "Figure: capstone team" }
---
<!-- src : CV ETH ; INVENTAIRE C et H (notes Obsidian « Capstone ECSE 458 »). Noms des coéquipiers non publiés (PLAN §11). -->

**TL;DR** — With three teammates, I am building an open tool that tells which transmission corridors in Québec, if they fail in an ice or wind storm, cause the most load to be shed — and which measures reduce that risk most. We started from an open PyPSA-Earth model of Hydro-Québec's grid built by a previous McGill student. I led the work that made its 315 kV version converge in AC power flow at all 168 hours of a winter test week, with every bus between 0.95 and 1.05 pu and a voltage-stable solution, cross-checked with pandapower. The main fix: line lengths had been measured in Web Mercator, 41 % to 66 % too long.
<!-- src : présentation « Québec grid model — progress for Prof. Wang (Nov. 17, 2026) » (Drive) : 168/168 h, 0,965–1,037 pu, ×1,41–1,66, pandapower ; diapo 18 : code produit sous la direction de Jean. Historique git : modèle et convergence 735 kV par nathan103004 (sept.-oct. 2026) → on n'écrit plus « I extended it down to 315 kV ». -->

<p class="stub-note">Full write-up coming this week.</p>
