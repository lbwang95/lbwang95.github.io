---
title: "Online Mobile Micro-Task Allocation in Spatial Crowdsourcing"
collection: publications
permalink: /publications/ICDE16
venue: "The 32nd International Conference on Data Engineering (ICDE)"
date: 16-20 May 2016
---
[[PDF]](http://lbwang95.github.io/files/icde16.pdf)

## Abstract
With the rapid development of smartphones, spatial crowdsourcing platforms are getting popular. A foundational research of spatial crowdsourcing is to allocate micro-tasks to suitable crowd workers. Most existing studies focus on offline scenarios, where all the spatiotemporal information of micro-tasks and crowd workers is given. However, they are impractical since micro-tasks and crowd workers in real applications appear dynamically and their spatiotemporal information cannot be known in advance. In this paper, to address the shortcomings of existing offline approaches, we first identify a more practical micro-task allocation problem, called the Global Online Micro-task Allocation in spatial crowdsourcing (GOMA) problem. We first extend the state-of-art algorithm for the online maximum weighted bipartite matching problem to the GOMA problem as the baseline algorithm. Although the baseline algorithm provides theoretical guarantee for the worst case, its average performance in practice is not good enough since the worst case happens with a very low probability in real world. Thus, we consider the average performance of online algorithms, a.k.a online random order model. We propose a two-phase-based framework, based on which we present the TGOA algorithm with 1 over 4 -competitive ratio under the online random order model. To improve its efficiency, we further design the TGOA-Greedy algorithm following the framework, which runs faster than the TGOA algorithm but has lower competitive ratio of 1 over 8. Finally, we verify the effectiveness and efficiency of the proposed methods through extensive experiments on real and synthetic datasets.
