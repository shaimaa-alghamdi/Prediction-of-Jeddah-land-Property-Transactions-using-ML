import string
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import sklearn
from joblib import dump, load
import xgboost as xgb
import re



st.title ("Prediction of Jeddah land Property Transactions")

neighborhood_dict = load('neighborhood_dict2.joblib')
#block_list = set(load('block_list.joblib'))

# Title
st.header("know about the Jeddah lands prices before investing!")


Re = re.compile(".*[أءإاضصثقفغعهخحجةشسيبلاتنمكظطذدزرو]{2}.*") 
Neighborhood_list = [n for n in list(neighborhood_dict) if Re.match(n) is not None]
Neighborhood = st.selectbox("Select the Neighborhood", Neighborhood_list)
block = st.selectbox("Select the block", neighborhood_dict[Neighborhood])
Area = st.number_input("Area of the land", 50)
d = st.date_input(
     "Date",
     datetime.date(2021, 1, 1), datetime.date(2021, 1, 1))

# If button is pressed
# Make prediction button
if st.button('Makek Prediction'):
   # Unpickle classifier
    model = load('model.joblib') 
    area_scaler = load('area_scaler1.joblib') 
    meter_price_scaler = load('meter_price_scaler.joblib') 
    neighborhood_dict = load('neighborhood_dict.joblib') 
    block_dict = load('block_dict.joblib') 
    columns = load('columns.joblib') 


    p_year = d.year - 2021
    # log then transform the area
    p_area = np.log(Area)
    p_area = area_scaler.transform(p_area.reshape(-1, 1))[0][0]

    neighborhood_index = neighborhood_dict[Neighborhood]
    block_index = block_dict[block]

    input_data = {
        f'neighborhood_{neighborhood_index}': 1,
        f'block_{block_index}': 1,
        'area': p_area,
        'year': p_year,
        'month': d.month,
        'day': d.day
    }

    for col in columns:
        if col not in input_data:
            input_data[col] = 0

    df_input = pd.DataFrame(input_data, index=[0], columns=columns)
    y_pred = model.predict(df_input)
    Calculate_SM = np.exp(meter_price_scaler.inverse_transform(y_pred[0].reshape(-1, 1)))
    y_actual = Calculate_SM * Area
    
     # show the results
    st.markdown(f"The land square meter price is <span style='color:#F0CEA3'>**{round(Calculate_SM [0][0])}**</span>", True)
    st.markdown(f"The land price is  <span style='color:#F0CEA3'>**{round(y_actual[0][0])}**</span>", True)

