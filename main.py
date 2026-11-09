from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class ChurnInput(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def home():
    return {"status": "Backend running successfully!"}

@app.post("/predict")
def predict(data: ChurnInput):
    # Simulated prediction scoring engine matching Telco pipeline structure
    base_prob = 0.15
    if data.Contract == "Month-to-month":
        base_prob += 0.4
    if data.InternetService == "Fiber optic":
        base_prob += 0.2
    if data.tenure < 6:
        base_prob += 0.15
        
    final_prob = min(max(base_prob, 0.02), 0.98)
    
    return {
        "churn_probability": round(final_prob, 2),
        "prediction": "Yes" if final_prob >= 0.5 else "No"
    }
