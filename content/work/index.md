---
title: Work
description: Projects in energy systems, robotics and research — Jean Flichy.
layout: work
intro: Six projects, from power systems modelling to an offshore converter station, followed by shorter projects and competitions. Detailed case studies are being added this week.
# Les 6 cartes principales viennent des pages content/work/*.md (champ `order`).
# Filtres (PLAN §5) : Energy · Robotics · Leadership · Research — attribués par le champ `filters`.
filters: [Energy, Robotics, Leadership, Research]
# More projects — source : 02 Contenu/brouillons/more-projects.md (faits ✅ ; les ⚠️ restent en commentaire).
more:
  - title: C-Blade — wing sails for cargo ships
    meta: CentraleSupélec · Year 1 entrepreneurship project · team of five · three months
    year: "2024"
    summary: A start-up simulation on decarbonising shipping with rigid wing sails. We compared rigid, soft, rotor and kite sails, scraped data on more than 4,000 ships built since 2015 to pick a target segment, designed a foldable 1,000 m² sail on a rotating base and built a first business case on EU carbon pricing.
    tags: [Shipping, Business plan]
    filters: [Energy]
    # src : Drive « C-Blade report V2 » ; brouillons/more-projects.md ; Jean (23/11) : projet d'entrepreneuriat de 1re année, 3 mois
  - title: Keeping a desert solar park clean
    meta: McGill · WCOM 206 business proposal
    year: "2025"
    summary: For a fictional energy consultancy, we proposed an electrostatic dust-removal system for the Quaid-e-Azam Solar Park in Pakistan's Cholistan desert (100 MW, about 400,000 panels). I wrote the literature review on how dust cuts panel output and worked out the power supply — one 3 kV supply per combiner box, about 0.75 W per panel.
    tags: [Solar, Technical writing]
    filters: [Energy]
    # src : Jean (23/11) ; INVENTAIRE I (392 158 modules ; 3 kV ; 0,75 W). Gains chiffrés non publiés (Jean, 23/11).
  - title: SmartBike — a navigation lamp for cyclists
    meta: McGill · INTG 215 · team of six · CTO and CFO
    year: "2025"
    summary: A start-up case for a bike lamp that also projects navigation arrows onto the road with a laser, so cyclists can keep their phone in their pocket. As CTO and CFO, I wrote the technical plan — a 55-week roadmap from prototype to a pilot batch — and the budget, a four-year financial plan (CAD 20 unit cost, CAD 30 wholesale price).
    tags: [Entrepreneurship, Product]
    filters: [Leadership]
    # src : présentation INTG215 (sources/2026-11-23) ; INVENTAIRE I ; rôle CTO et CFO (Jean, 23/11)
  - title: VizAdrift — could a boat drift home to France?
    meta: CentraleSupélec Modelling Week · two weeks
    year: "2024"
    summary: We studied North Atlantic weather regimes in historical data, coded a low-order atmospheric model (Charney–DeVore) in Python, measured its predictability with Lyapunov exponents and turned it into winds pushing a kite-towed boat from Montréal. Under a stable blocking regime it never reaches France; with westerly winds it can, in 35 to 100 days.
    tags: [Modelling, Weather]
    filters: [Research]
    # src : présentation finale VizAdrift (sources/2026-11-23). ⚠️ « validé sur 30 ans de données » retiré (cité comme amélioration future).
  - title: FloodViz — urban flooding
    meta: Coding Weeks, with Onepoint Bordeaux · two weeks
    year: "2023"
    summary: A Python tool that models urban flooding, optimises the sewer network and visualises the result. Winning team of the Coding Weeks; we presented it to the whole Onepoint team.
    tags: [Python, Water]
    filters: [Research]
    image: { base: /img/projects/floodviz-onepoint, h: 600, max_w: 1536, alt: "Students presenting slides titled Algorithm to an audience in Onepoint's offices" }
    # src : CV ETH (winning team) ; Jean (22/11) : présenté devant tout Onepoint ; photo du 17/11/2023. ⚠️ nom exact du prix : non publié
  - title: Radar modelling with Thales
    meta: CentraleSupélec Modelling Week · team of three · two weeks
    year: "2024–25"
    summary: Electronic beam steering for a coastal radar. We modelled a phased array, computed the phase shifts needed to sweep ±45° in azimuth, and cut the array to 24 emitters over 4 m — a full sweep in 0.036 s. A Hann window on the emitters limits false echoes from strong reflectors off to the side. Visiting Thales's radar site in Limours made me choose electrical engineering.
    tags: [Electromagnetism, Simulation]
    filters: [Research]
    # src : sources/2026-11-23/RADAR_beam_deflection_Thales_Modelling_Week.pdf ; année : 2e année (2024-25), Jean (23/11) → « 2025 »
  - title: Robotics Bootcamp — winning team
    meta: CentraleSupélec · one week
    summary: A robot that follows a line, avoids obstacles and follows a person.
    tags: [Robotics]
    filters: [Robotics]
    # ⚠️ année non confirmée : non affichée
  - title: Motor Challenge — winning team
    meta: CentraleSupélec Physics Challenge
    year: "2025"
    summary: An electric motor built from simple materials. The same challenge included a Rubens' tube, which shows standing sound waves as flames.
    tags: [Electrical machines, Physics]
    filters: [Energy]
  - title: FORGE Hack — 2nd place and Best Design Award
    meta: Hackathon
    year: "2026"
    summary: A robot that shoots basketballs into a hoop, designed and built during the hackathon.
    tags: [Robotics, Hackathon]
    filters: [Robotics]
    image: { base: /img/projects/forge-hack-robot, h: 600, max_w: 1600, alt: "Small wheeled robot on a green basketball-court mat with a miniature hoop" }
    # src : Jean (22/11) : mars 2026, robot qui marque des paniers de basket ; classement : CV ETH
  - title: IEEE Xtreme — Top 20 in Canada
    meta: 24-hour programming competition
    year: "2025"
    summary: IEEE's international 24-hour programming contest, November 2025.
    tags: [Programming, Competition]
    filters: []
    # src : Jean (22/11) : novembre 2025 ; classement : CV ETH
  - title: McGill Engineering Competition — 3rd place
    meta: Robot design competition
    year: "2025"
    summary: 3rd place in November 2025 with a wheeled robot built during the competition. I took part again in November 2026.
    tags: [Robotics, Competition]
    filters: [Robotics]
    image: { base: /img/projects/mec-2025-robot, h: 600, max_w: 1600, alt: "Wheeled robot covered in colourful jumper wires, held over a table" }
    # src : Jean (22/11) : 3e place en nov. 2025, participation aussi en nov. 2026 ; photo du 15/11/2025.
---
