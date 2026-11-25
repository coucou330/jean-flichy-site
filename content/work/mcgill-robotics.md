---
# Étape 5 (25/11) : étude de cas complète (brouillon + CV ETH + Sponsor Pres.pdf + robotics/shield_simulation&info ; faits ✅ INVENTAIRE D).
# Palmarès 2024-25 = contexte du club (avant le mandat), pas les succès de Jean. Co-directeur non nommé.
title: McGill Robotics
subtitle: Co-leading a 220-student team that builds a drone, a Mars rover and an underwater vehicle
layout: project
order: 3
card_meta: McGill University
year: 2025–
card_summary: Co-leading a 220-student team that builds a drone, a Mars rover and an underwater vehicle.
filters: [Robotics, Leadership]
dates: Member since September 2025 · Team Captain since 2026
where: McGill University, Montréal
team: 220 students, three robot projects
role: Team Captain (co-director); previously hydrophone electronics
tags: [Leadership, Robotics, Electronics]
tools: [MATLAB, LTspice]
description: Team Captain of McGill Robotics — 220 students, three robots, a CAD 100k budget back in the black after a CAD 30k deficit.
image: { base: /img/projects/robotics-auv-electronics, h: 500, max_w: 1600, alt: "Open red waterproof case packed with circuit boards and colour-coded cables", caption: "Inside the underwater vehicle's electronics enclosure.", credit: "" }
gallery:
  - { base: /img/projects/robotics-team, h: 1067, max_w: 1600, alt: "McGill Robotics members gathered in the team's workshop under a RoboSub 2025 banner", caption: "McGill Robotics in its workshop.", credit: "Photo: McGill Robotics", tall: true }
  - { base: /img/projects/robotics-captain-talk, h: 1067, max_w: 1600, alt: "Jean presenting in front of a screen to a room of students, seen from behind the audience", caption: "Presenting to members as Team Captain, September 2026.", credit: "", tall: true }
  - { base: /img/projects/robotics-scope, h: 600, max_w: 1600, alt: "Oscilloscope screen showing two green signal traces, one with a sharp burst", caption: "Bench test on the oscilloscope, April 2026.", credit: "" }
---
<!-- src générale : CV ETH ; robotics/Sponsor Pres.pdf (plaquette 2025-26) ; shield : Jean 09/11 (validé en simulation, tests en cours) + robotics/shield_simulation&info/shield_simulation.asc/.raw (analyse AC LTspice du 01/04/2026, lue le 25/11). -->

**TL;DR** — McGill Robotics is a student design team of 220 members building three competition robots. As Team Captain, I co-lead it with a co-director: we manage a CAD 100k budget, balanced this year for the first time after a CAD 30k deficit. Before taking the role, I designed the filter shield for the underwater vehicle's hydrophones, validated in simulation (MATLAB, LTspice); bench tests are under way.

## Context

The club runs three projects, each aimed at an international competition: an autonomous underwater vehicle (RoboSub), a Mars rover (Canadian International Rover Challenge) and a hybrid VTOL drone (Student Unmanned Aerial Systems competition). It also organises RoboHacks, a 24-hour robotics hackathon for CEGEP and undergraduate students, and outreach in schools.
<!-- src : Sponsor Pres.pdf (diapos 6-9) -->

The teams had done well before my term: first place for the design presentation at RoboSub 2025, first place in the science task at the Canadian International Rover Challenge 2025 (11th overall), and the Dawn Jaeger Tenacity Award at SUAS 2024. Those results belong to the members of those years.
<!-- src : Sponsor Pres.pdf — résultats d'équipe ANTÉRIEURS au mandat de Jean : présentés comme contexte du club (INVENTAIRE D) -->

## What I do as Team Captain

- **Co-lead the team** with a co-director: coordinate the three project teams and the business team, and represent the club to the faculty and to sponsors.
- **Manage a CAD 100k budget** from grants and sponsors. After a CAD 30k deficit, this is the club's first balanced year.
- **Outreach:** robotics workshops for 13-year-olds and talks in Montréal CEGEPs.
<!-- src : Sponsor Pres.pdf (diapo contacts : Robotics Co-Directors) ; CV ETH (budget, déficit) ; INVENTAIRE D (outreach) -->
<!-- ⚠️ Jean : 2-3 actions concrètes de ton mandat (plan de sponsoring, SSF Short Term Proposal F26, visibilité OIQ ?) — non publiées tant que non confirmées. -->

## What I built as a member: the hydrophone filter shield

The underwater vehicle locates an acoustic pinger, which emits between 25 and 40 kHz, by comparing the signals of several hydrophones. The hydrophone signals have to be amplified, and everything outside that band filtered out, before they can be processed. I designed that filtering stage.

- **Circuit.** A preamplifier, four band-pass filter stages and an output amplifier, built around op-amps.
- **Simulation.** In my LTspice model, the chain gives about 60 dB of gain across the 25–40 kHz band, while a 1 kHz signal comes out more than 100 dB lower. I also checked the design in MATLAB.
- **Status.** The design is validated in simulation; bench tests are under way.

[[figure:robotics-shield-response]]
<!-- src : CV ETH (25–40 kHz, MATLAB/LTspice, tests en cours) ; shield_simulation.asc (U1 gain 10 → 4 étages passe-bande à contre-réaction multiple U2-U5 → U6 gain 10) ; shield_simulation.raw (AC 1 k–100 kHz : ≈ 60,6 dB à 25 kHz, 59,6 dB à 32 kHz, 58,6 dB à 40 kHz ; −58,8 dB à 1 kHz, soit ≈ 119 dB sous la bande ; nœud de sortie identifié par Claude d'après le schéma). -->

## Results

- **RoboSub 2026:** 6th of 68 teams and 2nd in North America — a team result, from my year as a member.
- **Finances:** the club's first balanced year after a CAD 30k deficit.
- **Shield:** a filter design validated in simulation, now in bench testing.
<!-- src : CV ETH ; Jean 09/11 -->

<!-- « What I am learning » (formulation de Claude, sans source écrite de Jean) : non publié. Proposition à valider dans RETOURS-JEAN :
Leading volunteers is mostly about making it easy for 220 people to know what matters this week. A balanced budget is not glamorous, but it is what lets the next team build robots at all. -->
