import json

import streamlit as st
import pandas as pd
import requests
import time


@st.cache
def get_data():
    path = r'C:\Development\Coding\Streamlit\aq-webapp\cars.csv'
    return pd.read_csv(path)


def get_str_value():
    url = "http://127.0.0.1:5000/Solve"
    headers = {'Content-Type': 'application/json'}
    proxies = {"http": None, "https": None}
    response = requests.request("GET", url, headers=headers, proxies=proxies)
    if response.ok:
        # response_data = response.text
        if response.text == "Solve":
            for i in range(0,5):
                url = "http://127.0.0.1:5000/Status"
                response = requests.request("GET", url, headers=headers, proxies=proxies)
                print(i)
                placeholder = st.empty()
                with placeholder.container():
                    st.write("Running")
                time.sleep(2)
                placeholder.empty()
        url = "http://127.0.0.1:5000/View"
        response = requests.request("GET", url, headers=headers, proxies=proxies)
        print(response.text)
        st.write(response.text)
    else:
        print("Response not ok")
        print(response.text)
        return


df = get_data()

makes = df['make'].drop_duplicates()
make_choice = st.sidebar.selectbox('Select your vehicle:', makes)
models = df[df['make'].isin([make_choice])]['model'].drop_duplicates()
model_choice = st.sidebar.selectbox('', models)

st.button("Get Value", key=None, help=None, on_click=get_str_value, args=None, kwargs=None, disabled=False)
