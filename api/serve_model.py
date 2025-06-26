from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize app
app = FastAPI(title="Energy Efficiency Predictor")

# Load trained model
model = joblib.load("models/regression_model.pkl")

# Define request body schema
class InputData(BaseModel):
    Relative_Compactness: float
    Surface_Area: float
    Wall_Area: float
    Roof_Area: float
    Overall_Height: float
    Orientation: int
    Glazing_Area: float
    Glazing_Area_Distribution: int

@app.get("/")
def root():
    return {"message": "Welcome to the Energy Efficiency Regression API!"}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[ 
        data.Relative_Compactness,
        data.Surface_Area,
        data.Wall_Area,
        data.Roof_Area,
        data.Overall_Height,
        data.Orientation,
        data.Glazing_Area,
        data.Glazing_Area_Distribution
    ]])
    
    prediction = model.predict(features)
    return {
        "heating_load_prediction": round(float(prediction[0]), 2)
    }
