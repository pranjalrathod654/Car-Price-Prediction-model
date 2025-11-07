import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open('car_model.pkl', 'rb'))

# --- PAGE CONFIG ---
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")


st.markdown("### Get an instant estimate of your car’s resale value!")

st.markdown("---")

# --- LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("📅 Year of Manufacture", 2000, 2025, 2015)
    present_price = st.number_input("💰 Showroom Price (in lakhs)", 0.0, 50.0, 5.0)
    km_driven = st.number_input("🛣️ Kilometers Driven", 0, 500000, 20000)

with col2:
    fuel_type = st.selectbox("⛽ Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("👤 Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("⚙️ Transmission Type", ["Manual", "Automatic"])
    owner = st.selectbox("🚘 Owner Type", [0, 1, 2, 3])

# --- ENCODING ---
fuel_dict = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_dict = {"Dealer": 0, "Individual": 1}
trans_dict = {"Manual": 0, "Automatic": 1}

features = np.array([[year, present_price, km_driven,
                      fuel_dict[fuel_type],
                      seller_dict[seller_type],
                      trans_dict[transmission],
                      owner]])

# --- PREDICTION ---
if st.button("🔍 Predict Price"):
    prediction = model.predict(features)
    price = prediction[0]

    st.success(f"### 💵 Estimated Car Price: ₹ {price:,.2f} lakhs")

    st.balloons()
