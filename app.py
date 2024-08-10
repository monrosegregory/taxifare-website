import streamlit as st
import requests
import datetime
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''

## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
    # - date and time >>> 2014-07-06 19:18:00
    # - pickup longitude
    # - pickup latitude
    # - dropoff longitude
    # - dropoff latitude
    # - passenger count
# d = st.date_input("Pickup Date", datetime.date(2019, 7, 6))
# t = st.time_input("Pickup Time", datetime.time(8, 45))
pickup_date = st.date_input("Pickup Date", value=datetime.datetime(2014, 7, 6, 19, 18, 00))
pickup_time = st.time_input("Pickup Time", value=datetime.datetime(2014, 7, 6, 19, 18, 00))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('Insert Pickup Longitude', value=-73.950655)
pickup_latitude = st.number_input('Insert Pickup Latitude', value=40.783282)
dropoff_longitude = st.number_input('Insert Dropoff Longitude', value=-73.984365)
dropoff_latitude = st.number_input('Insert Dropoff Latitude', value=40.769802)
passenger_count = st.number_input('Insert Passenger Number', step=1, min_value=1, value=1)

# GREG https://taxifare-bhzbvqfkmq-ew.a.run.app/predict
# LEWAGON https://taxifare.lewagon.ai/predict

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('PREDICTION')

# 2. Let's build a dictionary containing the parameters for our API...
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

# 3. Let's call our API using the `requests` package...
call_api = requests.get(url, params=params)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...
st.markdown('Here is our prediction')
response_json = call_api.json()
st.write(response_json["fare"])

## Finally, we can display the prediction to the user

df = pd.DataFrame(
    [[pickup_latitude, pickup_longitude], [dropoff_latitude, dropoff_longitude]],
    columns=['lat', 'lon'])

st.map(df)
