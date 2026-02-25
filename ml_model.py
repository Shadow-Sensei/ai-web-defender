import joblib

# load once when file is imported
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(MODEL_PATH)

def predict_risk(features):
    """
    features = [requests, fails, avg_delta]
    returns float between 0 and 1
    """
    return model.predict_proba([features])[0][1]
