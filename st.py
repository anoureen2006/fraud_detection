import streamlit as st
import pandas as pd
import time

st.title("Real-Time Fraud Detection Monitor")


placeholder = st.empty()

while True:
   
    try:
        df = pd.read_csv("fraud_log.txt", names=["Prediction", "Amount"])
        
      
        count_fraud = len(df[df["Prediction"] == "FRAUD DETECTED"])
        count_legit = len(df[df["Prediction"] == "Legit"])
        
        
        with placeholder.container():
            
            kpi1, kpi2 = st.columns(2)
            
            kpi1.metric(label="Legit Transactions", value=count_legit)
            kpi2.metric(label="Frauds Caught", value=count_fraud)
            
           
            st.write("### Recent Transactions")
            st.dataframe(df.tail(10))
            
    except Exception as e:
        st.error(f"Waiting for data... ({e})")
        

    time.sleep(1)
