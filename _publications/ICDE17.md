---
title: "Trichromatic Online Matching in Real-Time Spatial Crowdsourcing"
collection: publications
permalink: /publications/ICDE17
venue: "The 33rd International Conference on Data Engineering (ICDE)"
date: 19-22 April 2017
---
[[PDF]](http://lbwang95.github.io/files/icde17.pdf)

## Abstract
The prevalence of mobile Internet techniques and Online-To-Offline (O2O) business models has led the emergence of various spatial crowdsourcing (SC) platforms in our daily life. A core issue of SC is to assign real-time tasks to suitable crowd workers. Existing approaches usually focus on the matching of two types of objects, tasks and workers, or assume the static offline scenarios, where the spatio-temporal information of all the tasks and workers is known in advance. Recently, some new emerging O2O applications incur new challenges: SC platforms need to assign three types of objects, tasks, workers and workplaces, and support dynamic real-time online scenarios, where the existing solutions cannot handle. In this paper, based on the aforementioned challenges, we formally define a novel dynamic online task assignment problem, called the trichromatic online matching in real-time spatial crowdsourcing (TOM) problem, which is proven to be NP-hard. Thus, we first devise an efficient greedy online algorithm. However, the greedy algorithm can be trapped into local optimal solutions easily. We then present a threshold-based randomized algorithm that not only guarantees a tighter competitive ratio but also includes an adaptive optimization technique, which can quickly learn the optimal threshold for the randomized algorithm. Finally, we verify the effectiveness and efficiency of the proposed methods through extensive experiments on real and synthetic datasets.
