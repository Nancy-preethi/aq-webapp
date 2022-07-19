import pandas as pd
import streamlit as st
import datetime
import time
from vic_stocks_view import fetch_stocks


tab1, tab2, tab3 = st.tabs(["HOME", "STOCK", "INSIDERS"])

with tab1:
    st.header("Home Page")
    df = pd.DataFrame()
    col1, col2 = st.columns([1,3])
    with col1:

        # -----------EARNINGS DATE --------------------
        st.write("Earnings Date")

        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=180)
        erng_start_date = st.date_input('Start date', today)
        erng_end_date = st.date_input('End date', tomorrow)
        if erng_start_date >= erng_end_date:
            st.error('Error: End date must fall after start date.')

        hasEarnings = st.checkbox('Has Earnings')
        hasOptions = st.checkbox('Has Options')
        vic = st.checkbox('VIC')
        insiders = st.checkbox('Insiders')
        hedgeFunds = st.checkbox('Hedge Funds')

        # -----------VIC DATE --------------------
        st.write("VIC Date")
        cur_today = datetime.date.today()
        vic_end = today + datetime.timedelta(days=180)
        vic_start_date = st.date_input('VIC Start date', cur_today)
        vic_end_date = st.date_input('VIC End date', vic_end)
        if vic_start_date < vic_end_date:
            col2.success('Start date: `%s`\n\nEnd date:`%s`' % (vic_start_date, vic_end_date))
        else:
            col2.error('Error: End date must fall after start date.')


        if st.button("Fetch Stocks"):
            df = fetch_stocks(erng_start_date, erng_end_date, hasEarnings, hasOptions, vic, insiders, hedgeFunds, vic_start_date, vic_end_date)
            col2.dataframe(df)

        if st.button("Export Data"):
            my_bar = col2.progress(0)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            df.to_csv('file_name.csv', index=False)
            col2.success("Completed.")
            col2.write("[Click Here](./file_name.csv) to view the file.")
        # st.empty()


with tab2:
    st.empty()
    st.header("Stock Details")
    stock_ticker = st.text_input('','')
    st.button("Fetch Stock Info")
    st.button("Fetch Option Return ")
    st.empty()

with tab3:

    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)




