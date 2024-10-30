import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(layout="wide")

scaler = StandardScaler()

st.title("Restaurant Rating Prediction")
st.caption("This app helps you predict a restaurant rating based on its features.")

st.divider()

average_cost = st.number_input("Please enter the estimated average cost for two", min_value=50, max_value=999999, value=1000, step=200)
tablebooking = st.checkbox("Restaurant has table booking", ["yes", "no"])
online_delivery = st.selectbox("Restaurant has online delivery", ["yes", "no"])
price_range = st.selectbox("What is the price range (1 Cheapest, 4 Expensive)", [1, 2, 3, 4])

