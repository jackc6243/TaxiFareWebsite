import streamlit as st
import datetime

'''
# TaxiFareModel Prediction
'''


'''
## Enter taxi ride information:
'''

d = st.date_input(
    "Enter your date of travel",
    datetime.datetime(2022, 1, 1, 1))

st.write(d)
t = st.time_input('Choose a time', datetime.time(8, 45))

date_time = datetime.datetime.combine(d, t).strftime("%Y-%m-%d %H:%M:%S")
st.write(date_time)

pickup_longitude = st.number_input('pickup longitude')
pickup_latitude = st.number_input('pickup latitude')
dropoff_longitude = st.number_input('dropoff longitude')
dropoff_latitude = st.number_input('dropoff latitude')
passenger_count = st.number_input('passenger count')

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'


'''
2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
data = {
    "pickup_latitude": pickup_latitude,
    "pickup_longitude": pickup_longitude,
    "dropoff_latitude": dropoff_latitude,
    "dropoff_longitude": dropoff_longitude,
    "passenger_count": passenger_count,
    "pickup_datetime": date_time,
}

import requests

response = requests.get(url, params=data)

"""
Result is:
"""

st.write(response.json())
