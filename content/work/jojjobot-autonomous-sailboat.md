---
# Étape 4 (24/11) : étude de cas complète (brouillon + AJOUTS 23/11 : revue d'avril 2025 ; faits ✅ INVENTAIRE C, H, I).
# ⚠️ Essais autonomes sur l'eau non confirmés : on écrit « designed to steer itself ».
title: JojjoBot — autonomous sailboat
card_title: JojjoBot
subtitle: A small sailboat designed to steer itself to a target using only the wind
layout: project
order: 4
card_meta: L2S, CentraleSupélec
year: "2025"
card_summary: An autonomous sailboat designed to steer itself to a target on wind power alone.
filters: [Robotics, Research, Leadership]
dates: January – July 2025
where: L2S laboratory (CNRS – CentraleSupélec – Université Paris-Saclay), Year 2 research project
team: Four students
role: Project lead; electronics and embedded software
supervisor: Prof. Thiago Alves Lima
tags: [Robotics, Control, Embedded systems]
tools: [Python, Raspberry Pi, I²C / UART / PWM, MATLAB/Simulink, FREE!ship]
description: JojjoBot — leading a team of four on an autonomous sailboat at the L2S laboratory; sensors, embedded Python on a Raspberry Pi and a controller ported from Simulink.
seo_description: "JojjoBot: leading a team of four on an autonomous sailboat at the L2S laboratory, with sensors, embedded Python and a controller ported from Simulink."
image: { base: /img/projects/jojjobot-hull, h: 500, max_w: 1600, alt: "Open hull of the small sailboat on a lab bench, with green 3D-printed brackets holding the electronics and a servo", caption: "The hull with its electronics installed, June 2025.", credit: "" }
gallery:
  - { base: /img/projects/jojjobot-bench, h: 600, max_w: 1600, alt: "Raspberry Pi, sensors and wiring on a cutting mat next to a laptop showing Python code", caption: "Integrating the sensors and the embedded Python code on the bench, April 2025.", credit: "" }
  - { base: /img/projects/jojjobot-hull-cad, h: 461, max_w: 864, alt: "Four views of the redesigned hull in the FREE!ship design software: perspective, profile, plan and body plan", caption: "The hull redesigned from 45 to 60 cm, after the plans of the RG65 radio-controlled class, to fit the electronics.", credit: "Figure: JojjoBot team" }
  - { base: /img/projects/jojjobot-jean, h: 1067, max_w: 1600, alt: "Jean sitting on the floor next to the sailboat, its mast and sail standing", caption: "With the boat, mast and sail rigged, June 2025.", credit: "" }
---
<!-- src générale : CV ETH ; Drive « Projet Jojjo » ; rapport « Report: Jojjobot – Automation and control » (Phase 2 = électronique, écrite par Jean) ; revue de mi-parcours du 11/04/2025 (sources/2026-11-23/JojjoBot_brief_deck_2025-04). -->
<!-- Corrections validées : PAS « self-learning » ; Thiago avec un h ; projet repris par le L2S. Noms des coéquipiers non publiés (PLAN §11). -->
<!-- ⚠️ Essais autonomes sur l'eau non confirmés (Jean ne sait pas) : on écrit « designed to steer itself », rien sur une navigation autonome réussie. -->

**TL;DR** — I led a team of four on a small sailboat designed to head for a GPS target on wind power alone. I integrated the electronics (Raspberry Pi, GPS, compass, wind sensors, servos), wrote the embedded Python code and ported the controller from Simulink to Python; the control law comes from a published nonlinear model of a sailboat. The L2S laboratory has continued the project after us.

## Context

Wind is one way to cut the emissions of shipping, and autonomy removes the need for a trained crew. We wanted a small, modular platform to test that idea — one that could later carry sensors for ocean monitoring. The project was our Year 2 research project at the L2S, the signals and systems laboratory of CentraleSupélec, supervised by Prof. Thiago Alves Lima.
<!-- src : rapport final (introduction) ; chiffres de contexte de la présentation (3 % des émissions…) non repris : sans source. -->

## My role

Project lead — planning, weekly meetings with our supervisor, presentations — and owner of the electronics and embedded software. Two teammates designed the control law in Simulink and one redesigned the hull; we all took part in the tests.
<!-- src : revue du 11/04/2025 (diapo 6 : répartition) ; Drive « Projet Jojjo » ; CV ETH (Project Lead) -->

## What I did

- **Designed the electronic architecture** from the inputs and outputs the controller needs: position (GPS), heading (compass), wind angle and wind speed (two Hall-effect rotary sensors); sail and rudder angles (two servo motors of more than 10 kg·cm), all run from a Raspberry Pi with an add-on board (HAT).
- **Got every sensor talking.** The GPS speaks UART, the compass and wind sensors I²C, the servos PWM. The two Hall-effect sensors shared the same I²C address, so I added a multiplexer; I calibrated the compass against nearby magnetic disturbances and set safe operating limits for each device.
- **Wrote a modular Python driver layer** — one class per device (servos, a threaded GPS reader, wind sensors, compass) behind a single `Boat` class — so that the control code only calls `get_heading()` or `set_rudder_angle()`.
- **Ported the controller from Simulink to Python** so that it runs on the boat: feedback linearisation with a hybrid automaton that switches between four headings to tack towards the target, plus a simpler PID version for comparison.
<!-- src : rapport final, Phase 2 (entrées/sorties, multiplexeur, calibration, classes, portage Simulink → Python, PID) ; revue d'avril (UART/I²C/PWM, HAT, servos > 10 kg·cm : INVENTAIRE H) ; modèle de L. Jaulin (CIFA 2004), automate hybride à 4 caps : INVENTAIRE C/H -->

[[include:diagram-jojjobot]]

The team also outgrew its first hull: at 45 cm it was too small for the components, so it was redesigned at 60 cm from the plans of the RG65 radio-controlled class, in the FREE!ship software, then thermoformed in two halves at La Fabrique, the school's fab lab, because the machine was limited to 50 cm.
<!-- src : revue d'avril, diapos 10-12 (INVENTAIRE I) ; « La Fabrique » = fablab de CentraleSupélec. -->

## Results

- In simulation, the controller guides the boat to a fixed target while keeping it stable; it is based on Luc Jaulin's nonlinear sailboat model.
- An assembled prototype — 60 cm hull, 3D-printed mounts, every sensor and actuator working together on the bench, under one Python interface.
- The L2S laboratory has continued the project since we finished.
<!-- src : rapport final (conclusion Phase 1, « Sailboat assembled ») ; CV ETH (repris par le labo) -->

## What I learned

Working with hardware that has little documentation means a lot of trial and error. I also learned to keep things simple: we had planned separate power regulation for the servos, then found that the circuit ran for hours on a single battery, so we kept the simpler design.
<!-- src : rapport final, Phase 2 (alimentation). -->
