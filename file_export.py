import pandas as pd
import streamlit as st
import time

# path = r'.\VIC Stocks_copy.csv'
# df = pd.read_csv(path)

name_dict = {
    'Name': ['a','b','c','d'],
    'Score': [90,80,95,20]
}

df = pd.DataFrame(name_dict)

if st.sidebar.button("Show Data"):
    st.table(df)

if st.sidebar.button("Export Data"):
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    df.to_csv('file_name.csv', index=False)
    st.success("Completed.")
    st.write("[Click Here](./file_name.csv) to view the file.")

