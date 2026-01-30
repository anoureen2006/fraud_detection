import joblib
import pandas as pd
import random


print("Loading model...")
model = joblib.load('model.pkl')


print("Loading a random transaction...")
df = pd.read_csv('creditcard.csv')


random_row = df.sample(1).drop('Class', axis=1)



print(f"Checking transaction details:\n{random_row.values}")


prediction = model.predict(random_row)

if prediction[0] == 0:
    print(">>> Prediction: LEGIT (0)")
else:
    print(">>> Prediction: FRAUD (1) !!!")
