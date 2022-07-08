import json

from PIL import Image
import streamlit as st
import pandas as pd
import requests
import time
primaryColor = st.get_option("theme.primaryColor")
s = f"""
<style>
div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; background-color: red; textColor: white;}}
<style>
"""
st.markdown(s, unsafe_allow_html=True)

@st.cache
def get_data():
    path = r'cars.csv'
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
    model_details_json = get_details(model_choice)
    # deserializing the data
    model_details = json.loads(model_details_json)

    print("Datatype after deserialization : "
      + str(type(model_details)))
    for m_name in model_details['model'].values():
        model_name = m_name
        st.write("SELECTED MODEL:",model_name)
        # break;
    for m_img_url in model_details['img_url'].values():
        model_img_url = m_img_url

        if model_img_url:
            image = Image.open(model_img_url)
            st.image(image)
        else:
            st.write("Image not found")