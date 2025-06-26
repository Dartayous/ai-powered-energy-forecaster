import pandas as pd
import joblib

# Load model
model = joblib.load("models/regression_model.pkl")

# Load new data
new_data = pd.read_csv("data/processed/new_samples.csv")

# Predict
predictions = model.predict(new_data)
print("Predictions:", predictions)
