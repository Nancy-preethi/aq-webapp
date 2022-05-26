from PIL import Image
import streamlit as st
import pandas as pd
import requests
import time


@st.cache
def get_data():
    path = r'C:\Development\Coding\Streamlit\aq-webapp\cars.csv'
    return pd.read_csv(path)


def get_details(model_choice):
    url = "http://127.0.0.1:5000/Solve"
    headers = {'Content-Type': 'application/json'}
    proxies = {"http": None, "https": None}
    response = requests.request("GET", url, headers=headers, proxies=proxies)
    if response.ok:
        # response_data = response.text
        if response.text == "Solve":
            my_bar = st.progress(0)

            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1)

        url = "http://127.0.0.1:5000/View?model="+model_choice
        response = requests.request("GET", url, headers=headers, proxies=proxies)
        return response.text
    else:
        print("Response not ok")
        print(response.text)
        return response.text


df = get_data()

makes = df['make'].drop_duplicates()
make_choice = st.sidebar.selectbox('Select your vehicle:', makes)
models = df[df['make'].isin([make_choice])]['model'].drop_duplicates()
model_choice = st.sidebar.selectbox('', models)

if st.sidebar.button("Submit"):
    model_img_url = get_details(model_choice)
    if model_img_url:
        image = Image.open(model_img_url)
        st.image(image)
    else:
        st.write("")