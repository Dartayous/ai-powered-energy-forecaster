![AI-Powered Energy Forecaster](Energy_Forecaster_Banner.png)

# AI-Powered Energy Forecaster 🔋⚡

A production-grade machine learning pipeline designed to forecast building heating loads using architectural and environmental data. Built with performance, clarity, and explainability in mind, this project combines FastAPI, scikit-learn, and SHAP for real-time inference and transparent model interpretation.

Ideal for roles in **AI engineering**, **machine learning development**, or **data-driven energy analysis**, this repo highlights:

- Deployment-ready model serving with FastAPI
- Batch prediction automation via client scripts
- End-to-end explainability with SHAP visualizations
- Clean modular code for scaling and refinement

Whether you're evaluating predictive modeling skills, backend API integration, or AI explainability, this project reflects a strong foundation in applied machine learning practices.

---

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/FastAPI-HighPerformance-green.svg" alt="FastAPI Badge"/>
  <img src="https://img.shields.io/badge/scikit--learn-MachineLearning-orange.svg" alt="scikit-learn Badge"/>
  <img src="https://img.shields.io/badge/SHAP-Explainability-purple.svg" alt="SHAP Badge"/>
  <img src="https://img.shields.io/badge/pandas-DataScience-lightgrey.svg" alt="pandas Badge"/>
</p>

---
### 🚀 Features

- Trains and evaluates a regression model on real-world energy data
- Serves predictions via a FastAPI endpoint at `/predict`
- Batch testing with `predict_client.py` for real-time inference
- SHAP integration to visualize feature contributions per prediction
- Heatmaps and pairplots for model + data storytelling
- Notebook included: `ai_powered_energy_forecaster.ipynb`

---

### 📂 Repo Structure

```bash
├── api/                    # FastAPI app to serve the model
├── models/                 # Training scripts and saved .pkl model
├── inference/              # Lightweight prediction interface
├── outputs/                # Batch predictions and SHAP visuals
├── ai_powered_energy_forecaster.ipynb  # EDA + SHAP notebook
├── predict_client.py       # POSTs sample payloads to API
├── requirements.txt
└── README.md

📄 License
This project is licensed under the MIT License — feel free to use, modify, and share it as long as you include proper attribution.

👤 Author
Created by Dartayous — blending cinematic storytelling and AI engineering to deliver intelligent, creative tech.

🔗 GitHub Profile

🧠 [LinkedIn or personal portfolio link if you want to include it later]