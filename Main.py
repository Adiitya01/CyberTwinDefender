# app/main.py
from fastapi import FastAPI
from app.schemas import IDSInput, EmailInput
import pickle
import numpy as np

app = FastAPI()

# Load models
with open("app/models/ids_model.pkl", "rb") as f:
    ids_model = pickle.load(f)

with open("app/models/phishing_model.pkl", "rb") as f:
    email_model = pickle.load(f)

@app.get("/")
def root():
    return {"message": "Intrusion & Email Detection API Running"}

@app.post("/predict/ids")
def predict_ids(data: IDSInput):
    features = np.array([[ 
        data.Flow_Duration,
        data.Total_Fwd_Packets,
        data.Total_Backward_Packets,
        data.Flow_Bytes_s,
        data.Flow_IAT_Mean,
        data.Packet_Length_Mean,
        data.Packet_Length_Std,
        data.Fwd_Packet_Length_Mean,
        data.Init_Win_Bytes_Forward,
        data.PSH_Flag_Count,
        data.ACK_Flag_Count
    ]])
    pred = ids_model.predict(features)[0]
    return {"prediction": "Attack" if pred == 1 else "Normal"}

@app.post("/predict/email")
def predict_email(data: EmailInput):
    vect_text = vectorizer.transform([data.text])
    pred = email_model.predict(vect_text)[0]
    return {"prediction": "Phishing" if pred == 1 else "Safe"}