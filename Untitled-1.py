# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib # This library saves the model

# 1. Load the data
# TODO: Read the 'data/creditcard.csv' file into a pandas DataFrame
print("Loading data...")
df= pd.read_csv('creditcard.csv')


# 2. Preprocessing
# TODO: Separate features (X) and target (y)
# Note: The target column in this dataset is 'Class'
Y=df['Class']
X=df.drop('Class',axis=1)

# TODO: Split into training and testing sets (use test_size=0.2)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print("Splitting data...")

# 3. Train the model

# TODO: Initialize a RandomForestClassifier (keep it simple for now, maybe n_estimators=10)
model=RandomForestClassifier(n_estimators=10,random_state=42)
print("Training model...")
# TODO: Fit the model on your training data
model.fit(X_train, y_train)

from sklearn.metrics import classification_report, accuracy_score # Import these

# ... (After clf.fit step) ...

# 5. Evaluate the model
print("Evaluating model...")
# Ask the model to predict the test set
y_pred = model.predict(X_test)

# Calculate accuracy (just for reference)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Print the detailed report (Precision, Recall, F1-Score)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# ... (Now you can Save the model) ...
# 4. Save the model

# This is the new part!
print("Saving model...")
joblib.dump(model, "model.pkl") # Replace 'model' with your variable name

print("Model saved successfully as 'model.pkl'")