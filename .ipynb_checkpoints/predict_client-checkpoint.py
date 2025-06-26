import requests
import csv

# Define the API endpoint
url = "http://127.0.0.1:8000/predict"

# Batch of input samples
samples = [
    {
        "Relative_Compactness": 0.98,
        "Surface_Area": 514.5,
        "Wall_Area": 294.0,
        "Roof_Area": 110.25,
        "Overall_Height": 7.0,
        "Orientation": 2,
        "Glazing_Area": 0.1,
        "Glazing_Area_Distribution": 3
    },
    {
        "Relative_Compactness": 0.75,
        "Surface_Area": 637.1,
        "Wall_Area": 318.5,
        "Roof_Area": 122.5,
        "Overall_Height": 3.5,
        "Orientation": 4,
        "Glazing_Area": 0.4,
        "Glazing_Area_Distribution": 5
    },
    {
        "Relative_Compactness": 0.82,
        "Surface_Area": 553.5,
        "Wall_Area": 318.5,
        "Roof_Area": 122.5,
        "Overall_Height": 7.0,
        "Orientation": 3,
        "Glazing_Area": 0.3,
        "Glazing_Area_Distribution": 2
    }
]

# Define output CSV file
output_file = "outputs/batch_predictions.csv"

# Write headers + predictions
with open(output_file, mode="w", newline="") as csv_file:
    fieldnames = list(samples[0].keys()) + ["heating_load_prediction"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i, sample in enumerate(samples, 1):
        response = requests.post(url, json=sample)
        if response.status_code == 200:
            prediction = response.json().get("heating_load_prediction", None)
            sample["heating_load_prediction"] = prediction
            writer.writerow(sample)
            print(f"✅ Sample {i} saved with prediction: {prediction}")
        else:
            print(f"❌ Sample {i} failed with status code {response.status_code}")
