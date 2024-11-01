import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(layout="wide")

scaler = joblib.load("scaler.pkl")

st.title("Restaurant Rating Prediction")
st.caption("This app helps you predict a restaurant rating based on its features.")

st.divider()

average_cost = st.number_input("Please enter the estimated average cost for two", min_value=50, max_value=999999, value=1000, step=200)
tablebooking = st.checkbox("Restaurant has table booking", ["yes", "no"])
online_delivery = st.selectbox("Restaurant has online delivery", ["yes", "no"])
price_range = st.selectbox("What is the price range (1 Cheapest, 4 Expensive)", [1, 2, 3, 4])

predict_button = st.button("Predict the rating")

st.divider()

model = joblib.load("model.pkl")

bookingstatus = 1 if tablebooking == "Yes" else 0
delivery = 1 if online_delivery == "Yes" else 0

values = [[average_cost, bookingstatus, delivery, price_range]]
my_x_values = np.array(values)

X = scaler.transform(my_x_values)

if predict_button:
    st.snow()
    prediction = model.predict(X)

    st.write(prediction)