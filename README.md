# climate-analysis
Exploring weather data using SQLite, SQLAlchemy, and Flask

### Table of Contents
- [1 Overview](#1-overview)
- [2 Results](#2-results)
- [3 Summary](#3-summary)


## 1 Overview

The purpose of this project was to conduct a weather analysis for the island of Oahu to potentially start a Surf and Shake Shop - serving surfboards and icecream to locals and tourists. However, to get some real investor backing to get the business off the ground, W. Avy was excited in the possibility in partnering together. One concern he had was the weather and asked that we conduct an analysis on a weather dataset he has from Oahu to determine if the island is indeed the ideal location for the shop.


## 2 Results

<p align="center">
  <img src="https://user-images.githubusercontent.com/95978097/156495669-789a730e-4e35-4277-9155-f96aa548d763.png" />
  <img src="https://user-images.githubusercontent.com/95978097/156495740-94a6a9c4-3a29-4966-b632-aa55d13c0b03.png" />
</p>

To determine if the surf and shake shop would be sustainable year round, W Avy asked that we analyze two months - June and December. Based on the results, the following information can be derived:

- the month of June had 183 more observations than the month of December (1700 in June vs. 1517 in December)
- the mean temperature for the month of June was 74.9 degrees, whereas December's was 71.0
- the minimum temperature for the month of June was 64 degrees and December was 56 degrees
- the maximum temperature for the month of June was 83 degrees and December was 85 degrees

## 3 Summary

Overall, based on the results, Oahu is a good fit to run a sustainable, year round surf and shake shop. Even while December had 183 less observations than June, it can be assumed that any missing data would not have significantly changed the results for the month. It is to be expected that in winter months (December), temperatures are cooler than in summer months (June). But, since Oahu is well-known to be a vacation destination primarily for its consistent weather, the temperature differentials are not extreme. To be certain, two additional queries were created to ensure
that the weather was ideal for the shop: 

<p align="center"> Retrieving precipitation measurements for June and December</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/95978097/156495166-cae7956b-ef3f-44bd-a44a-f4af38f80be3.png" />
  <img src="https://user-images.githubusercontent.com/95978097/156495217-6f11ad1b-45ca-4998-a65f-2784ce7a4de3.png" />
</p>

<p align="center"> Determine which of active station(s) recorded temperature and precipitation data for June and December</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/95978097/156498636-1beab0d3-8c9f-45bb-9fa9-d90fde4fdfb2.png" />
  <img src="https://user-images.githubusercontent.com/95978097/156498746-2df17077-85aa-4dc9-a6c1-d14b79619f92.png" />
</p>

Both June and December had some precipitation but based on the temperature results, even with precipitation, temperatures remain relatively warm and suitable for both surfing and ice cream. Additionally, based on the most active stations list retrieved in the module, all 9 stations recorded weather data for June and December.

