import streamlit as st
import requests

API_URL = "http://localhost:8000/predict" 

st.set_page_config(page_title="Telco Churn Predictor", page_icon="📊")
st.title("📊 Telco Customer Churn Predictor")

with st.form("churn_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["0", "1"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)
    total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=600.0)
    submit_button = st.form_submit_button("Predict Churn Probability")

if submit_button:
    payload = {
        "gender": gender, "SeniorCitizen": int(senior_citizen), "Partner": partner, 
        "Dependents": dependents, "tenure": int(tenure), "PhoneService": phone_service,
        "MultipleLines": multiple_lines, "InternetService": internet_service,
        "OnlineSecurity": online_security, "OnlineBackup": online_backup,
        "DeviceProtection": device_protection, "TechSupport": tech_support,
        "StreamingTV": streaming_tv, "StreamingMovies": streaming_movies,
        "Contract": contract, "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method, "MonthlyCharges": float(monthly_charges),
        "TotalCharges": float(total_charges)
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            prob = result.get("churn_probability", 0.0)
            if prob >= 0.5:
                st.error(f"🚨 **High Risk:** {prob*100:.1f}% probability")
            else:
                st.success(f"✅ **Low Risk:** {prob*100:.1f}% probability")
            st.progress(float(prob))
        else:
            st.error(f"Backend API Error: {response.text}")
    except Exception as e:
        st.error(f"Connect failed: {e}")
