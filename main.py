from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Initialize the App
app = FastAPI(title="Fraud Detection API")

# 2. Load the Model (The "Brain")
# We load it here so it stays in memory and doesn't reload for every request
print("Loading model...")
model = joblib.load('model.pkl')

# 3. Define the Input Format
# This tells the API: "Expect a JSON object with a list of numbers called 'features'"
class Transaction(BaseModel):
    features: list[float]  # Expecting a list of floats (Time, V1-V28, Amount)

# 4. Define the Prediction Endpoint
@app.post("/predict")
def predict_fraud(transaction: Transaction):
    # Convert list to a numpy array (reshaped for the model)
    # The model expects a 2D array: [[val1, val2, ...]]
    features_array = np.array(transaction.features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features_array)
    
    # Return result
    if prediction[0] == 0:
        return {"prediction": "Legit", "fraud_flag": 0}
    else:
        return {"prediction": "FRAUD DETECTED", "fraud_flag": 1}

# 5. Root Endpoint (Just to check if app is running)
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running!"}