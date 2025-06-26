import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json
import os

from models.model_utils import save_metrics

# Load data
df = pd.read_csv("data/raw/energy_efficiency.csv")

# Feature/target split
X = df.drop(columns=["Y1", "Y2"])  # Y1 = Heating Load, Y2 = Cooling Load
y = df["Y1"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

# Save model
joblib.dump(model, "models/regression_model.pkl")

# Save metrics
save_metrics(rmse, r2)
