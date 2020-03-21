---
title: "Dynamic Pricing in Spatial Crowdsourcing: A Matching-Based Approach"
collection: publications
permalink: /publications/SIGMOD18
venue: "2018 37th ACM SIGMOD International Conference on Management of Data (SIGMOD)"
date: June 10-15, 2018
---
[[PDF]](http://lbwang95.github.io/files/sigmod18.pdf)

## Abstract
In spatial crowdsourcing, requesters submit their task-related locations and increase the demand of a local area. The platform prices these tasks and assigns spatial workers to serve if the prices are accepted by requesters. There exist mature pricing strategies which specialize in tackling the imbalance between supply and demand in a local market. However, in global optimization, the platform should consider the mobility of workers; that is, any single worker can be the potential supply for several areas, while it can only be the true supply of one area when assigned by the platform. The hardness lies in the uncertainty of the true supply of each area, hence the existing pricing strategies do not work. In the paper, we formally define this <u>G</u>lobal <u>D</u>ynamic <u>P</u>ricing(GDP) problem in spatial crowdsourcing. And since the objective is concerned with how the platform matches the supply to areas, we let the matching algorithm guide us how to price. We propose a *MAtching-based Pricing Strategy* (MAPS) with guaranteed bound. Extensive experiments conducted on the synthetic and real datasets demonstrate the effectiveness of MAPS.