from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class Features(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: Features):
    X = np.array(data.features).reshape(1, -1)
    prediction = model.predict(X)
    return {"prediction": int(prediction[0])}
