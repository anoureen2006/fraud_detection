import streamlit as st
import pandas as pd
import time

st.title("Real-Time Fraud Detection Monitor")

# Create a placeholder element on the page
placeholder = st.empty()

while True:
    # 1. Read the data
    # We use header=None because we just appended raw lines
    try:
        df = pd.read_csv("fraud_log.txt", names=["Prediction", "Amount"])
        
        # 2. Calculate simple stats
        count_fraud = len(df[df["Prediction"] == "FRAUD DETECTED"])
        count_legit = len(df[df["Prediction"] == "Legit"])
        
        # 3. Update the UI inside the placeholder
        with placeholder.container():
            # Create three columns for metrics
            kpi1, kpi2 = st.columns(2)
            
            kpi1.metric(label="Legit Transactions", value=count_legit)
            kpi2.metric(label="Frauds Caught", value=count_fraud)
            
            # detailed view
            st.write("### Recent Transactions")
            st.dataframe(df.tail(10)) # Show last 10 rows
            
    except Exception as e:
        st.error(f"Waiting for data... ({e})")
        
    # 4. Wait before refreshing
    time.sleep(1)