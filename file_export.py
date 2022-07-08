import datetime
import time

import pandas as pd
import streamlit as st

# path = r'.\VIC Stocks_copy.csv'
# df = pd.read_csv(path)
from vic_stocks_view import fetch_stocks

df = pd.DataFrame()
# -----------EARNINGS DATE --------------------
st.sidebar.write("Earnings Date")

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=180)
erng_start_date = st.sidebar.date_input('Start date', today)
erng_end_date = st.sidebar.date_input('End date', tomorrow)
if erng_start_date >= erng_end_date:
    st.error('Error: End date must fall after start date.')

hasEarnings = st.sidebar.checkbox('Has Earnings')
hasOptions = st.sidebar.checkbox('Has Options')
vic = st.sidebar.checkbox('VIC')
insiders = st.sidebar.checkbox('Insiders')
hedgeFunds = st.sidebar.checkbox('Hedge Funds')


# -----------VIC DATE --------------------
st.sidebar.write("VIC Date")
cur_today = datetime.date.today()
vic_end = today + datetime.timedelta(days=180)
vic_start_date = st.sidebar.date_input('VIC Start date', cur_today)
vic_end_date = st.sidebar.date_input('VIC End date', vic_end)
if vic_start_date < vic_end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (vic_start_date, vic_end_date))
else:
    st.error('Error: End date must fall after start date.')


if st.sidebar.button("Fetch Stocks"):
    df = fetch_stocks(erng_start_date, erng_end_date, hasEarnings, hasOptions, vic, insiders, hedgeFunds, vic_start_date, vic_end_date)
    st.dataframe(df)

if st.sidebar.button("Export Data"):
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    df.to_csv('file_name.csv', index=False)
    st.success("Completed.")
    st.write("[Click Here](./file_name.csv) to view the file.")

