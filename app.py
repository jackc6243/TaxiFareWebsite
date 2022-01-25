import streamlit as st
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Enter pick up and drop off location:

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
d = st.date_input(
    "Enter your date of travel",
    datetime.datetime(2022, 1, 1, 1, 1, 1))
#t = st.time_input('Set an alarm for', datetime.time(8, 45))
pickup_longitude = st.number_input('pickup longitude')
pickup_latitude = st.number_input('pickup latitude')
dropoff_longitude = st.number_input('dropoff longitude')
dropoff_latitude = st.number_input('dropoff latitude')
passenger_count = st.number_input('dropoff latitude')

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
    "pickup_datetime": d,
}

import requests

response = requests.get(url, params=data)

st.write(response.json())