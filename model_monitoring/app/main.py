'''
Streamlit app to do the following:
    - Track data drift of model inputs
    - Monitor the load of api endpoints

TODO:
    - Add endpoint load graph
    - Add more monitoring tools
    - Generalize to apply for other models
'''
import requests
import streamlit as st
import os
import altair as alt
import pandas as pd

from db import connect_to_postgres, get_postgres_data

# Attempt to load from database. Make up initial data if table is empty.
try:
    engine = connect_to_postgres()
    query = "SELECT * FROM dummy_predictions"
    dummy_pred_data = get_postgres_data(query, engine)
except:
    dummy_pred_data = pd.DataFrame(
        data={
            'gender': [0],
            'age': [30],
            'bmi': [25.0]
        }
    )


st.title('Dummy Underwriting Monitoring')


# Histogram of inputs
st.text("Histogram to track distribution of prediction inputs.")
if st.button('Update Data Pull'):
    engine = connect_to_postgres()
    query = "SELECT * FROM dummy_predictions"
    dummy_pred_data = get_postgres_data(query, engine)

input_to_plot = st.selectbox("Histogram Selection", ["gender", "age", "bmi"])
input_hist = alt.Chart(dummy_pred_data).mark_bar().encode(
    alt.X(input_to_plot + ":Q", bin=True),
    y='count()',
)
st.altair_chart(input_hist, use_container_width=True)


# Sidebar inputs
st.sidebar.title("Perform prediction")
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
issue_age = st.sidebar.number_input('Issue Age', 18, 80, 30)
bmi = st.sidebar.number_input('BMI', 10.0, 50.0, 24.5, 0.1)

# Sidebar button & output
if st.sidebar.button('Submit'):
    url = 'http://nginx:8080/dummy/v0.0/predict'
    gender_binary = 0
    if gender == 'Female':
        gender_binary = 1
    data = {'gender': gender_binary, 'age': issue_age, 'bmi': bmi}
    resp = requests.post(url, json=data)
    if resp.json()["outcome"] == "approved":
        resp_outcome = "You have been approved!"
    elif resp.json()["outcome"] == "declined":
        resp_outcome = "Sorry, you have been declined."
    else:
        resp_outcome = "Service down. Please try again later."
    st.sidebar.write(resp_outcome)
