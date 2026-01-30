import joblib
import pandas as pd
import random

# 1. Load the saved model (The "Brain")
print("Loading model...")
model = joblib.load('model.pkl')

# 2. Load data just to grab a random example
# In a real app, this data would come from the user/website, not the CSV
print("Loading a random transaction...")
df = pd.read_csv('creditcard.csv')

# Pick a random row, but drop the 'Class' (answer) column
random_row = df.sample(1).drop('Class', axis=1)

# 3. specific "Fraud" test (Optional)
# If you want to see if it catches a fraud, uncomment the lines below:
# frauds = df[df['Class'] == 1]
# random_row = frauds.sample(1).drop('Class', axis=1)

print(f"Checking transaction details:\n{random_row.values}")

# 4. Predict
prediction = model.predict(random_row)

if prediction[0] == 0:
    print(">>> Prediction: LEGIT (0)")
else:
    print(">>> Prediction: FRAUD (1) !!!")