# Prediction-of-Jeddah-land-Property-Transactions-using-ML


## Goal 
Goal: There is a significant movement in property transactions in Jeddah city, especially the lands. Therefore, there is a need for an ML model to predict property prices based on the neighborhood, block, area and date.

## The Dataset
This dataset allows clients to find out the data on transactions conducted in cities during a certain time period (monthly, quarterly, or annual). The indicators measure the number of transactions, the number of properties, the value in Saudi riyals, the area in square meters, and the value of square meter. They enable monitoring the status of property transactions in various cities, finding out the most active cities, viewing the average price of property and the price of square meter, and comparing with different cities. They also enable easy monitoring of the details and values of transactions conducted in cities, and include 24 indicators as follows:

- Monthly (8 indicators)
- Quarterly (8 indicators)
- Annual (8 indicators)

The dataset is collected from [Ministry of Justice][https://www.moj.gov.sa/ar/opendata/bi/birealestate/Dashboards/200_kpiTown/201_Monthly/kpi201_04_G.aspx]. I will choose Jeddah city with all districts as a sample training the model. In addition, the dataset period is from Jan 1, 2021, to Aug 3, 2022 which is the last update from Ministry of Justice


The observations of the dataset were descriped using 9 features as follows:


| features | description |
| --------------- | --------------- | 
| City | The city where land locate |
| Neighborhood | The neighborhood where land locate in |
| Block | The block of the land |
| Land_number |The details of the land (e.g, A/122)|
| Date| The Land transaction date|
| id |The number of each land transaction|
| Area| The land area in square meters|
| Square_meter_price | The Value of a square meter| 
| Full_price |The transaction price in Saudi Riyals SR| 
