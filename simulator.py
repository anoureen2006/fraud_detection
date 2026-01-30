import pandas as pd
import requests
import time
import json


print("Loading data for simulation...")
df = pd.read_csv('creditcard.csv')


fraud_samples = df[df['Class'] == 1].sample(20)
legit_samples = df[df['Class'] == 0].sample(80)
# Combine and shuffle them
stream_data = pd.concat([fraud_samples, legit_samples]).sample(frac=1).reset_index(drop=True)

# 2. Define the API Endpoint (Where your Docker container is listening)
url = "http://127.0.0.1:8000/predict"

print("Starting traffic simulation... Press Ctrl+C to stop.")
print("-" * 50)


for index, row in stream_data.iterrows():
    
    features = row.drop('Class').tolist()
    
   
    payload = {"features": features}
    
    try:
     
        response = requests.post(url, json=payload)
        

        result = response.json()
        prediction = result['prediction']
        
        
        if prediction == "FRAUD DETECTED":
            print(f"Transaction {index}: \033[91m⚠️  FRAUD DETECTED!\033[0m")
        else:
            print(f"Transaction {index}: \033[92m✅ Legit\033[0m")
       
        with open("fraud_log.txt", "a") as f:
            amount=time.ctime()
            f.write(f"{prediction},{amount}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Is your Docker container running?")
        break
        
   
    time.sleep(0.5)
