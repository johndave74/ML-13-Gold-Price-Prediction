# ML-13-Gold-Price-Prediction
This project provides an end-to-end machine learning solution for predicting gold prices using historical market data. It includes data analysis, model building, and a deployed Streamlit app for real-time predictions.

---

## 🏆 **Gold Price Prediction App**

This project provides an end-to-end machine learning solution for predicting gold prices using historical market data. It includes data analysis, model building, and a deployed Streamlit app for real-time predictions.

---

### 📊 **Project Overview**

* **Goal:** To build a machine learning model that predicts the price of gold based on key market indicators such as SPX (S\&P 500 index), USO (oil prices), SLV (silver prices), and EUR/USD (currency exchange rate).
* **Approach:**

  * Exploratory Data Analysis (EDA) on historical gold prices.
  * Correlation analysis to identify key predictors.
  * Model training using a regression algorithm (Random Forest Regressor).
  * Deployment via a **Streamlit web app** for user interaction.

---

## 🔍 **Insights from the Analysis**

The analysis conducted in the `main.ipynb` notebook revealed several key findings:

-  **High Correlation with SPX:**
A negative correlation was observed between the S\&P 500 index (SPX) and gold prices, indicating that gold often serves as a hedge during stock market downturns.

-  **Influence of USO and SLV:**
Oil (USO) and silver (SLV) prices showed positive correlations with gold prices, reflecting commodity market dynamics.

-  **Exchange Rate Impact:**
The EUR/USD currency pair also had a measurable influence, suggesting sensitivity of gold prices to currency fluctuations.

-  **Feature Importance:**
The Random Forest model highlighted SPX and USO as the most significant predictors for gold price.

---

## **The Machine Learning Model**

* **Algorithm:** Random Forest Regressor
* **Training Data:** Historical gold price dataset with market indicators
* **Target Variable:** `GLD` (Gold Price)
* **Features Used:**

  * SPX (S\&P 500 Index)
  * USO (Oil Fund Price)
  * SLV (Silver Fund Price)
  * EUR/USD (Currency Exchange Rate)

The model achieved a high accuracy (R² score) during validation, indicating strong predictive capability.

---

## 🌐 **The Streamlit Web App**

The `app.py` file powers a user-friendly web interface for gold price prediction:

✨ **Key Features:**

* Interactive **sidebar input** for the four predictor variables.
* Real-time prediction with **`Predict Gold Price`** button.
* Displays the **predicted price** dynamically.
* Embedded **custom CSS styling** for enhanced UI aesthetics.
* Option to load and display the original dataset.
* Easily extendable to fetch live gold prices via API integration (currently commented out in the code for customization).

---

## 🚀 **How to Run Locally**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/gold-price-prediction-app.git
   cd gold-price-prediction-app
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

> ✅ Ensure `gold_price_model.pkl` and `gld_price_data.csv` are in the project directory.

---

## 📦 **Files Included**

| File                   | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| `main.ipynb`           | Data exploration, analysis, and model training notebook |
| `app.py`               | Streamlit web app source code                           |
| `gold_price_model.pkl` | Trained machine learning model                          |
| `gld_price_data.csv`   | Dataset with historical gold prices                     |

---

## 📝 **Possible Enhancements**

* Enable **real-time data fetching** via external APIs for up-to-date predictions.
* Integrate **additional features** (e.g., interest rates, inflation indexes).
* Deploy on **cloud platforms** (Streamlit Sharing, Heroku, AWS).



### 🤝 **Contact**

Created by: **John David**

For inquiries or collaborations: adelekejohndavid@gmail.com
