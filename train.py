# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib 


print("Loading data...")
df= pd.read_csv('creditcard.csv')



Y=df['Class']
X=df.drop('Class',axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print("Splitting data...")

model=RandomForestClassifier(n_estimators=10,random_state=42)
print("Training model...")

model.fit(X_train, y_train)

from sklearn.metrics import classification_report, accuracy_score 


print("Evaluating model...")

y_pred = model.predict(X_test)


print(f"Accuracy: {accuracy_score(y_test, y_pred)}")


print("Classification Report:")
print(classification_report(y_test, y_pred))


print("Saving model...")
joblib.dump(model, "model.pkl") 

print("Model saved successfully as 'model.pkl'")
