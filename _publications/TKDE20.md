---
title: "Two-sided Online Micro-Task Assignment in Spatial Crowdsourcing"
collection: publications
permalink: /publications/TKDE20
venue: "IEEE Transactions on Knowledge and Data Engineering (TKDE)"
---
[[PDF]](http://lbwang95.github.io/files/tkde20.pdf)

## Abstract
With the rapid development of smartphones, spatial crowdsourcing platforms are getting popular. A foundational research of spatial crowdsourcing is to allocate micro-tasks to suitable crowd workers. Many existing studies focus on the offline scenario, where all the spatiotemporal information of micro-tasks and crowd workers is given. In this paper, we focus on the online scenario and identify a more practical micro-task allocation problem, called the Global Online Micro-task Allocation in spatial crowdsourcing (GOMA) problem. We first extend the state-of-the-art algorithm for the online maximum weighted bipartite matching problem to the GOMA problem as the baseline algorithm. Although the baseline algorithm provides a theoretical guarantee for the worst case, its average performance in practice is not good enough since the worst case happens with a very low probability in the real world. Thus, we consider the average performance of online algorithms, a.k.a. random order model. We propose a two-phase-based framework, based on which we present the TGOA algorithm with a 1/4 -competitive ratio under the random order model. To improve its efficiency, we further design the TGOA-Greedy and TGOA-OP algorithm following this framework, which runs faster than the TGOA algorithm with a competitive ratio of 1/8 and 1/4 , respectively. We also revisit the average performance of Greedy, which has long been considered as the worst due to its unbounded competitive ratio in the worst case. Finally, we verify the effectiveness and efficiency of the proposed methods through extensive experiments on synthetic and real datasets.
