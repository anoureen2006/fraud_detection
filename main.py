from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Initialize the App
app = FastAPI(title="Fraud Detection API")


print("Loading model...")
model = joblib.load('model.pkl')


class Transaction(BaseModel):
    features: list[float]  # Expecting a list of floats (Time, V1-V28, Amount)


@app.post("/predict")
def predict_fraud(transaction: Transaction):
    # Convert list to a numpy array (reshaped for the model)
    # The model expects a 2D array: [[val1, val2, ...]]
    features_array = np.array(transaction.features).reshape(1, -1)
    
   
    prediction = model.predict(features_array)
    
   
    if prediction[0] == 0:
        return {"prediction": "Legit", "fraud_flag": 0}
    else:
        return {"prediction": "FRAUD DETECTED", "fraud_flag": 1}


@app.get("/")
def home():
    return {"message": "Fraud Detection API is running!"}
