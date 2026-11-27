---
# Étape 4 (24/11) : étude de cas complète (brouillon + présentation à Prof. Wang du 17/11/2026, faits ✅ INVENTAIRE C, H, I).
title: Québec grid resilience
subtitle: How far can an extreme winter push Québec's transmission grid before load must be shed?
layout: project
order: 1
card_meta: Capstone, McGill
year: 2026–27
card_summary: How far can an extreme winter push Québec's grid before load must be shed?
filters: [Energy, Research]
dates: September 2026 – April 2027 (in progress)
where: McGill University, Montréal · ECSE 458 Capstone Design Project
team: Four students
role: Grid modelling and AC power flow
supervisor: Prof. Xiaozhe Wang
tags: [Energy, Power systems, Modelling]
tools: [Python, PyPSA, pandapower, OpenStreetMap data, Hydro-Québec open data]
description: Capstone project. An open model of Québec's 735 and 315 kV grid made to converge in AC power flow at every hour of a winter week, as the base for studying cascading failures in ice and wind storms.
seo_description: "Capstone project: an open model of Québec's 735 and 315 kV grid made to converge in AC power flow, as the base for studying cascading failures in storms."
image: { base: /img/projects/capstone-peak-voltages, h: 500, max_w: 1600, alt: "Map of the Québec 735 kV and 315 kV network model, buses coloured by voltage at the January 2022 peak hour", caption: "Our corrected model at the peak hour of the test week (3 January 2022, 17:00): every bus voltage, 735 kV and 315 kV lines.", credit: "Figure: capstone team" }
gallery_layout: wide
gallery:
  - { base: /img/projects/capstone-line-lengths, h: 294, max_w: 1600, alt: "Scatter plot showing stored line lengths about 1.4 to 1.7 times too long as latitude increases, and a bar chart comparing 735 kV kilometres in the model with Hydro-Québec's inventory", caption: "Why the AC model diverged: line lengths had been measured in Web Mercator, which stretches them by 1/cos(latitude). They came out 41% to 66% too long.", credit: "Figure: capstone team" }
  - { base: /img/projects/capstone-test-week, h: 378, max_w: 1600, alt: "Hourly demand of the January 2022 test week above the band of bus voltages in the model", caption: "The test week, 1–7 January 2022: Hydro-Québec demand (top) and the range of bus voltages in the model at every hour (bottom).", credit: "Figure: capstone team" }
  - { base: /img/projects/capstone-load-margin, h: 347, max_w: 1600, alt: "P-V curves of the lowest bus voltage as load and generation are scaled up at the peak hour", caption: "Load margin at the peak hour: voltage, not line ratings, sets the limit.", credit: "Figure: capstone team" }
---
<!-- src : CV ETH ; INVENTAIRE C, H et I ; brouillon quebec-grid-resilience.md (bloc « AJOUT 23/11 » = présentation « Québec grid model — progress for Prof. Wang (Nov. 17, 2026) », Drive). Noms des coéquipiers et de l'auteur du modèle de départ non publiés (PLAN §11). -->

With three teammates, I am building an open tool that finds which transmission corridors in Québec cause the most load to be shed if they fail in an ice or wind storm, and which measures reduce that risk most. We started from an open model of Hydro-Québec's grid built by a previous McGill student. I led the work that made its 315 kV version converge in AC power flow at all 168 hours of a winter test week, with a voltage-stable solution cross-checked by three solvers. The main fix was in the line lengths, which had been measured in Web Mercator and were 41% to 66% too long.
<!-- Rôle : historique git = modèle 315 kV et convergence 735 kV par l'auteur du modèle de départ (sept.-oct. 2026) ; l'équipe, sous la direction de Jean (16-17/11), a fait converger le 315 kV. On n'écrit pas « I extended it down to 315 kV » (⚠️ CV ETH à corriger par Jean). -->

## Context

Hydro-Québec runs one of the largest hydro-dominated grids in the world. Very long 735 kV lines carry power from the dams of the north to the cities of the south, and the 1998 ice storm showed how exposed those corridors are. Winters already test the grid, and climate change may make storms more severe.

Research on cascading failures in storms usually works on small textbook networks such as the IEEE 39-bus system. We want to apply it to a model of the real Québec grid, built only from open data, so that anyone can check and reuse it.
<!-- src : Proposed project — schema.md (Gerkis & Wang 2025 : IEEE 39-bus ; nous : réseau HQ réel) ; abstract du projet (Capstone.md) -->

## What I did

Our starting point is a PyPSA-Earth model of Hydro-Québec's 735 kV and 315 kV network, built from OpenStreetMap and Hydro-Québec data by a previous McGill student. Its 735 kV version already solved in AC power flow. The 315 kV version, which a realistic resilience study needs, did not.

I directed the code the team wrote to make that 315 kV model converge in AC power flow at every hour of a winter test week (1–7 January 2022). Each hour had to pass the same checks: the Newton solver converges, generators stay within their reactive-power limits, every bus voltage stays between 0.95 and 1.05 pu, and the solution is voltage-stable.

The divergence came from the map projection. Line lengths in the starting model had been measured in Web Mercator, which stretches distances by 1/cos(latitude). At Québec's latitudes every line came out 41% to 66% too long, and its reactance and charging with it. We recomputed every length as a true geodesic distance.

To make sure the convergence is not an artefact of one tool, we cross-checked the results with PyPSA, pandapower and a third independent solver. I also audited the model's assumptions one by one against Hydro-Québec's public data (line lengths, thermal ratings, demand). Each one is rated solid, reasonable or fragile, with the data we would need to fix the fragile ones.
<!-- src : présentation du 17/11 (168/168 h ; 5 critères ; Web Mercator ×1,41–1,66 ; 3 solveurs ; diapo 18 : code produit sous la direction de Jean) ; notes Obsidian « Hypothèses du modèle » (audit). Compensation série / SVC / réactances shunt : présentes dans le modèle (CV ETH, INVENTAIRE C), non attribuées à Jean ici par prudence. -->

## Results so far

- An AC-feasible model of Québec's high-voltage grid built entirely from open data. All 168 hours of the test week converge, every bus voltage stays between 0.965 and 1.037 pu, and the three solvers agree.
- A first load margin. At the peak hour the model stays stable up to 37.4 GW, a 7% margin, and the limit comes from voltage around western Montréal rather than from line ratings. The real grid has carried more than that on its coldest days, which tells us exactly which data the open model still lacks.
- A list of the model's weakest assumptions and of the data needed to fix them.
<!-- src : présentation du 17/11 (0,965–1,037 pu ; +7% ; 37,4 GW ; Montréal-Ouest). Record réel cité dans la présentation (43,1 GW le 03/02/2023) non publié : chiffre non revérifié contre une source Hydro-Québec. ⚠️ N-1 / N-2 (axe Churchill → Côte-Nord) : non publié. -->

## What comes next

[[include:diagram-capstone]]

1. **A better base model.** Rebuild the network from OpenStreetMap with corrected line data.
2. **From storm to failures.** Fragility curves give the probability that a line fails under a given ice load or wind speed; we apply them hour by hour through a storm.
3. **Cascades.** An AC cascading-failure model (protections, islanding, load shedding), run over thousands of storm scenarios.
4. **Metrics and design.** Rank the critical corridors, then compare mitigation strategies on the same metrics: hardening lines, reactive compensation, series compensation, preventive redispatch before a storm.

The project runs until April 2027.
<!-- src : Proposed project — schema.md ; présentation du 17/11 (« Suite : reconstruire depuis OpenStreetMap, puis AC-CFM »). -->

## What I am learning

An earlier version of the model already converged while its lines were 41% to 66% too long. So a model that solves can still be wrong. We only found the error because we kept asking *why* each correction was needed and whether it matched the real grid.
<!-- Formulation à relire par Jean (RETOURS-JEAN). -->
