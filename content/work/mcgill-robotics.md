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
role: Team Captain (co-director) and hydrophone lead
tags: [Leadership, Robotics, Electronics]
tools: [MATLAB, LTspice]
description: Team Captain of McGill Robotics — 220 students, three robots, a CAD 100k budget back in the black after a CAD 30k deficit, and hydrophone lead.
image: { base: /img/projects/robotics-auv-electronics, h: 500, max_w: 1600, alt: "Open red waterproof case packed with circuit boards and colour-coded cables", caption: "Inside the underwater vehicle's electronics enclosure.", credit: "" }
gallery:
  - { base: /img/projects/robotics-team, h: 1067, max_w: 1600, alt: "McGill Robotics members gathered in the team's workshop under a RoboSub 2025 banner", caption: "McGill Robotics in its workshop.", credit: "Photo: McGill Robotics", tall: true }
  - { base: /img/projects/robotics-captain-talk, h: 1067, max_w: 1600, alt: "Jean presenting in front of a screen to a room of students, seen from behind the audience", caption: "Presenting to members as Team Captain, September 2026.", credit: "", tall: true }
  - { base: /img/projects/robotics-scope, h: 600, max_w: 1600, alt: "Oscilloscope screen showing two green signal traces, one with a sharp burst", caption: "Bench test on the oscilloscope, April 2026.", credit: "" }
---
<!-- src générale : CV ETH ; robotics/Sponsor Pres.pdf (plaquette 2025-26) ; shield : Jean 09/11 (validé en simulation, tests en cours) + robotics/shield_simulation&info/shield_simulation.asc/.raw (analyse AC LTspice du 01/04/2026, lue le 25/11). -->

**TL;DR** — McGill Robotics is a student design team of 220 members building three competition robots. As Team Captain, I co-lead it with a co-director: we approve budgets, chair the executive meetings, organise team-wide events and run the business team. We manage a CAD 100k budget, balanced this year for the first time after a CAD 30k deficit, and have already raised more than CAD 25,000 this year. I also lead the hydrophone sub-team, whose filter shield I designed as a member: a PCB is now in testing.

## Context

The club runs three projects, each aimed at an international competition: an autonomous underwater vehicle (RoboSub), a Mars rover (Canadian International Rover Challenge) and a hybrid VTOL drone (Student Unmanned Aerial Systems competition). It also organises RoboHacks, a 24-hour robotics hackathon for CEGEP and undergraduate students, and outreach in schools.
<!-- src : Sponsor Pres.pdf (diapos 6-9) -->

The teams had done well before my term: first place for the design presentation at RoboSub 2025, first place in the science task at the Canadian International Rover Challenge 2025 (11th overall), and the Dawn Jaeger Tenacity Award at SUAS 2024. Those results belong to the members of those years.
<!-- src : Sponsor Pres.pdf — résultats d'équipe ANTÉRIEURS au mandat de Jean : présentés comme contexte du club (INVENTAIRE D) -->

## What I do as Team Captain

- **Run the club** with a co-director: we approve the budgets, chair the executive meetings and coordinate the three project teams.
- **Organise the team-wide events:** design reviews, networking events, orientation day, recruitment events and fundraisers.
- **Lead the business team**, which handles partnerships, grant applications and communication. This year we have already raised more than CAD 25,000.
- **Represent the club** to the faculty, our partners and our main sponsors, whom we meet regularly; we also handle practical matters such as merchandise orders.
- **Manage a CAD 100k budget** from grants and sponsors. After a CAD 30k deficit, this is the club's first balanced year.
- **Outreach:** robotics workshops for 13-year-olds and talks in Montréal CEGEPs.
<!-- src : Sponsor Pres.pdf (diapo contacts : Robotics Co-Directors) ; CV ETH (budget, déficit) ; INVENTAIRE D (outreach) -->
<!-- src : Jean (25/11, en conversation) : approbation des budgets, events team-wide (design reviews, networking, orientation day), présidence des réunions d'execs, business team (partenariats, subventions, communication), > 25 000 $ obtenus cette année, events de recrutement, fundraisers, réunions partenaires et gros sponsors, représentation, commandes de merch. -->

## The hydrophone filter shield: from member to lead

The underwater vehicle locates an acoustic pinger, which emits between 25 and 40 kHz, by comparing the signals of several hydrophones. The hydrophone signals have to be amplified, and everything outside that band filtered out, before they can be processed. I designed that filtering stage.

<!-- src : Jean (25/11) : hydrophone lead cette année, supervise les 4 nouveaux membres ; problème compris, PCB designé, en phase de test. -->
- **Circuit.** A preamplifier, four band-pass filter stages and an output amplifier, built around op-amps.
- **Simulation.** In my LTspice model, the chain gives about 60 dB of gain across the 25–40 kHz band, while a 1 kHz signal comes out more than 100 dB lower. I also checked the design in MATLAB.
- **This year, as hydrophone lead,** I supervise four new members. We have pinned down the whole problem, designed a PCB for the shield and are now testing it.

[[figure:robotics-shield-response]]
<!-- src : CV ETH (25–40 kHz, MATLAB/LTspice, tests en cours) ; shield_simulation.asc (U1 gain 10 → 4 étages passe-bande à contre-réaction multiple U2-U5 → U6 gain 10) ; shield_simulation.raw (AC 1 k–100 kHz : ≈ 60,6 dB à 25 kHz, 59,6 dB à 32 kHz, 58,6 dB à 40 kHz ; −58,8 dB à 1 kHz, soit ≈ 119 dB sous la bande ; nœud de sortie identifié par Claude d'après le schéma). -->

## Results

- **RoboSub 2026:** 6th of 68 teams and 2nd in North America — a team result, from my year as a member.
- **Finances:** the club's first balanced year after a CAD 30k deficit, and more than CAD 25,000 raised so far this year.
- **Hydrophones:** a filter design validated in simulation, now on a PCB in testing, with a sub-team of four new members.
<!-- src : CV ETH ; Jean 09/11 -->

<!-- « What I am learning » (formulation de Claude, sans source écrite de Jean) : non publié. Proposition à valider dans RETOURS-JEAN :
Leading volunteers is mostly about making it easy for 220 people to know what matters this week. A balanced budget is not glamorous, but it is what lets the next team build robots at all. -->
