# Prediction-of-Jeddah-land-Property-Transactions-using-ML


## Introduction
Although the companies and ministries in Saudi Arabia have started publishing their datasets on open source platforms, there is a lack of analysis and the use of artificial intelligence techniques. This is due to difficulties in analyzing the Arabic dataset, which contains various values and needs complex cleaning operations to reach satisfactory results.


## This project follows five steps:
- Get of data from a Ministry of Justice website.
- Data preprocessing such as (dealing with NAN values and repeated rows).
- Generate insights and plot Arabic labels in the correct formatting as possible.
- Train and test the model using different ML models.
- Comparison between the applied models.
- Deploy machine learning model in production.

## Project Goal 
There is a significant movement in property transactions in Jeddah city, especially the lands. Therefore, there is a need for an ML model to predict property prices based on the neighborhood, block, area and date.

- Generate insights about the land transactions in Jeddah city (EDA).
- Integrate of ML model into an existing production environment where it can take in an input and return an output with the best ML model performed.

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



## value proposition
This project will help the Ministry of Justice and the citizens understand the current land transactions conducted in Jeddah city and predict the price of these transactions in Saudi riyals.

## Test the app
[Test the app][https://shaimaa-alghamdi-prediction-of-jeddah-land-property--app-pthmne.streamlitapp.com/]





