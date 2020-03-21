---
title: "Flexible online task assignment in real-time spatial data"
collection: publications
permalink: /publications/VLDB17
venue: "Proceedings of the VLDB Endowment Vol. 10, No. 11"
date: August 2017
---
[[PDF]](http://lbwang95.github.io/files/vldb17.pdf)

## Abstract
The popularity of Online To Offline (O2O) service platforms has spurred the need for online task assignment in real-time spatial data, where streams of spatially distributed tasks and workers are matched in real time such that the total number of assigned pairs is maximized. Existing online task assignment models assume that each worker is either assigned a task immediately or waits for a subsequent task at a fixed location once she/he appears on the platform. Yet in practice a worker may actively move around rather than passively wait in place if no task is assigned. In this paper, we define a new problem <u>F</u>lexible <u>T</u>wo-sided <u>O</u>nline task <u>A</u>ssignment (FTOA). FTOA aims to guide idle workers based on the prediction of tasks and workers so as to increase the total number of assigned worker-task pairs. To address the FTOA problem, we face two challenges: (i) How to generate guidance for idle workers based on the prediction of the spatiotemporal distribution of tasks and workers? (ii) How to leverage the guidance of workers' movements to optimize the online task assignment? To this end, we propose a novel two-step framework, which integrates offline prediction and online task assignment. Specifically, we estimate the distributions of tasks and workers per time slot and per unit area, and design an online task assignment algorithm, <u>P</u>rediction-oriented <u>O</u>nline task <u>A</u>ssignment in <u>R</u>eal-time spatial data (POLAR-OP). It yields a 0.47-competitive ratio, which is nearly twice better than that of the state-of-the-art. POLAR-OP also reduces the time complexity to process each newly-arrived task/worker to O(1). We validate the effectiveness and efficiency of our methods via extensive experiments on both synthetic datasets and real-world datasets from a large-scale taxi-calling platform.