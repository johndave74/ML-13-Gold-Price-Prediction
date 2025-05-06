# Streamlit app for Gold Prediction
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from streamlit.components.v1 import html
import requests

# Function to fetch the latest gold price
# def fetch_latest_gold_price():
#     url = "https://www.metals-api.com/api/latest"
#     params = {
#         "access_key": "YOUR_API_KEY",
#         "base": "USD",  # Base currency
#         "symbols": "XAU"  # Gold symbol
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         return data['rates']['XAU']
#     else:
#         st.error("Failed to fetch the latest gold price.")
#         return None

# Load the model
model = joblib.load('gold_price_model.pkl')

# Function to predict gold price
def predict_gold_price(features):
    # Convert features to DataFrame
    features_df = pd.DataFrame([features])
    # Predict using the model
    prediction = model.predict(features_df)
    return prediction[0]

# Apply custom CSS
def apply_custom_css():
    css = """
    <style>
        body {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333333;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
    """
    html(css, height=0)
    #st.markdown(css, unsafe_allow_html=True)

# Apply CSS
apply_custom_css()

# Streamlit app layout
st.title("Gold Price Prediction App")
st.write("This app predicts the future price of gold based on historical data.")

# Load and display the dataset
data = pd.read_csv('gld_price_data.csv')

# Input features
with st.sidebar:
    st.subheader("Input Features")
    st.write("Please enter the following features to predict the gold price:")

    # Example input fields (replace with actual features from your model)
    feature1 = st.number_input("Feature 1 (e.g., SPX)", min_value=0.0, step=0.1)
    feature2 = st.number_input("Feature 2 (e.g., USO)", min_value=0.0, step=0.1)
    feature3 = st.number_input("Feature 3 (e.g., SLV)", min_value=0.0, step=0.1)
    feature4 = st.number_input("Feature 4 (e.g., EUR/USD)", min_value=0.0, step=0.01)

# Predict button
if st.button("Predict Gold Price"):
    features = {
        "Feature1": feature1,
        "Feature2": feature2,
        "Feature3": feature3,
        "Feature4": feature4
    }
    prediction = predict_gold_price(features)
    st.success(f"The predicted gold price is: ${prediction:.2f}")