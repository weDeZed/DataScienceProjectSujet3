from fastapi import FastAPI, HTTPException
from api.schemas.input import PredictionInput
from api.utils.loader import load_model, predict_with_model, get_model_info
import pandas as pd
from sklearn import ensemble
import pickle
import os
from pydantic import BaseModel


app = FastAPI(
        title="API Prédiction Marketing",
        description="""
Cette API prédit les ventes à partir des budgets marketing (TV, Radio, Social Media, Influenceur).

**Entrée pour /predict :**
```
{
    "tv": float,           # Budget TV
    "radio": float,        # Budget Radio
    "social_media": float, # Budget Social Media
    "influencer": float    # Influenceur (score ou encodé)
}
```
""",
        version="1.0.0"
)

# Load model at startup
# Load model at startup (can be None)
the_model = load_model()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/model-info")
def model_info():
    info = get_model_info(the_model)
    if "error" in info:
        raise HTTPException(status_code=503, detail=info["error"])
    return info

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        prediction = predict_with_model(the_model, input_data)
        return {"prediction": prediction}
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
