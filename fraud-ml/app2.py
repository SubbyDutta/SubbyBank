from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load saved model and scaler
model = joblib.load("loan_model.pkl")
scaler = joblib.load("scaler.pkl")

class LoanRequest(BaseModel):
   
    income: float
    pan: str
    adhar: str
    credit_score: float
    requested_amount: float
    balance: float
    avg_transaction: float

@app.post("/predictloan")
def predict_loan(data: LoanRequest):
    # Convert to DataFrame for model
    df = pd.DataFrame([{
        "income": data.income,
        "credit_score": data.credit_score,
        "requested_amount": data.requested_amount,
        "balance": data.balance,
        "avg_transaction": data.avg_transaction
        # note: PAN & Adhar are categorical; you could encode if your model used them
    }])
    
    # Scale numeric features
    df_scaled = scaler.transform(df)
    
    # Predict eligibility
    pred_prob = model.predict_proba(df_scaled)[:,1][0]
    eligible = bool(model.predict(df_scaled)[0])
    
    return {
       
        "eligible": eligible,
        "probability": pred_prob
    }
