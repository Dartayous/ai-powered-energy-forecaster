import json
import os

def save_metrics(rmse, r2, path="outputs/metrics.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump({"RMSE": rmse, "R2": r2}, f, indent=4)
