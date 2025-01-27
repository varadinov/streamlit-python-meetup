import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_random_data():
    today = datetime.today()
    last_month = today - timedelta(days=30)
    date_range = pd.date_range(start=last_month, end=today, freq='h')  # Hourly data
    data = pd.DataFrame({
        'datetime': date_range,
        'value': np.random.randint(1, 100, size=len(date_range))
    })
    return data


st.title("Datetime Filter with Chart")


data = generate_random_data()

st.sidebar.header("Filter Data by Date")
start_date = st.sidebar.date_input("Start Date", value=data['datetime'].min().date())
end_date = st.sidebar.date_input("End Date", value=data['datetime'].max().date())

# Ensure the user input is valid
if start_date > end_date:
    st.error("Start date must be before end date.")
else:
    # Filter the data
    filtered_data = data[
        (data['datetime'] >= pd.to_datetime(start_date)) &
        (data['datetime'] <= pd.to_datetime(end_date))
    ]

    # Chart with the filtered data
    st.write("### Chart of Filtered Data")
    st.line_chart(filtered_data.set_index('datetime')['value'])