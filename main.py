import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pickle import load
from pathlib import Path
from settings import settings

app = FastAPI(title="Iris Classification API")


with open(Path(settings.model_path), "rb") as f:
    MODEL = load(f)


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class PredictionOutput(BaseModel):
    class_id: int
    class_name: str


class HealthOutput(BaseModel):
    status: str
    model_version: str


@app.get("/health")
def health_check(response_model=HealthOutput):
    return {"status": "ok", "model_version": settings.model_version}


@app.post("/predict", response_model=PredictionOutput)
def predict(data: IrisInput):
    try:
        features = np.array([[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]])
        prediction_index = MODEL.predict(features)[0]
        predicted_class = settings.target_names[prediction_index]
        return {
            "class_id": int(prediction_index),
            "class_name": predicted_class
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))