from pydantic import BaseModel
from typing import Any

class PredictionInput(BaseModel):
    # Remplacer ces champs par ceux attendus par le modèle
    feature1: float
    feature2: float
    # Ajouter d'autres features selon le modèle
