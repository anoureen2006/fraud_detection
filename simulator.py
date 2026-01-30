import pandas as pd
import requests
import time
import json

# 1. Load the data (to simulate incoming transactions)
print("Loading data for simulation...")
df = pd.read_csv('creditcard.csv')

# Get a mix of legit and fraud transactions to make it interesting
# We grab 20 random fraud cases and 80 random legit cases
fraud_samples = df[df['Class'] == 1].sample(20)
legit_samples = df[df['Class'] == 0].sample(80)
# Combine and shuffle them
stream_data = pd.concat([fraud_samples, legit_samples]).sample(frac=1).reset_index(drop=True)

# 2. Define the API Endpoint (Where your Docker container is listening)
url = "http://127.0.0.1:8000/predict"

print("Starting traffic simulation... Press Ctrl+C to stop.")
print("-" * 50)

# 3. Loop through the data
for index, row in stream_data.iterrows():
    # Convert row to list (exclude the 'Class' label, because the API doesn't know the answer!)
    features = row.drop('Class').tolist()
    
    # Prepare the payload
    payload = {"features": features}
    
    try:
        # Send POST request to your Docker API
        response = requests.post(url, json=payload)
        
        # Parse response
        result = response.json()
        prediction = result['prediction']
        
        # Print status
        # We color-code output: RED for Fraud, GREEN for Legit (using ANSI codes)
        if prediction == "FRAUD DETECTED":
            print(f"Transaction {index}: \033[91m⚠️  FRAUD DETECTED!\033[0m")
        else:
            print(f"Transaction {index}: \033[92m✅ Legit\033[0m")
        # Inside your loop, after getting the result:
        with open("fraud_log.txt", "a") as f:
            amount=time.ctime()
            f.write(f"{prediction},{amount}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Is your Docker container running?")
        break
        
    # Wait a bit to simulate real-time traffic (0.5 seconds)
    time.sleep(0.5)