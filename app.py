import streamlit as st
from decision import predict_loan

st.set_page_config(
    page_title="Loan Eligibility Predictor",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Eligibility Prediction System")

st.write("Enter customer details below:")

age = st.number_input("Age", min_value=18, max_value=100, value=25)
income = st.number_input("Annual Income", min_value=0, value=50000)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=700)
loan_amount = st.number_input("Loan Amount", min_value=0, value=100000)

if st.button("Check Eligibility"):

    result = predict_loan(
        age,
        income,
        credit_score,
        loan_amount
    )

    if result == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")