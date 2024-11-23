import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# Load the scaler and model objects from files
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

# Create the Streamlit app layout and title
st.title("Restaurant Rating Prediction")
st.caption("This app helps you predict a restaurant rating based on its features.")

# Create input fields for user to enter restaurant features
average_cost = st.number_input(
    "Please enter the estimated average cost for two", 
    min_value=50, 
    max_value=999999, 
    value=1000, 
    step=200
)
tablebooking = 1 if st.checkbox("Restaurant has table booking") else 0
online_delivery = 1 if st.selectbox("Restaurant has online delivery", ["Yes", "No"]) == "Yes" else 0
price_range = st.selectbox(
    "What is the price range (1 Cheapest, 4 Expensive)", 
    [1, 2, 3, 4]
)

# Create a button to trigger the prediction
predict_button = st.button("Predict the rating")

# Define the prediction logic
if predict_button:
    # Prepare and scale the input values
    values = [[average_cost, tablebooking, online_delivery, price_range]]
    X = scaler.transform(np.array(values, dtype=float))  # Ensure numeric format
    
    # Make a prediction using the model object
    prediction = model.predict(X)
    
    # Display the prediction result
    st.write(f"Predicted Rating: {prediction[0]}")
    # Display the corresponding rating
    if prediction < 2.5:
        st.write("Rating: Poor")
    elif prediction < 3.5:
        st.write("Rating: Average")
    elif prediction < 4.0:
        st.write("Rating: Good")
    elif prediction < 4.5:
        st.write("Rating: Very Good")
    else:
        st.write("Rating: Excellent")
