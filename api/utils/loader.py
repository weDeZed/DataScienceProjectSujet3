import pickle
import os
from api.schemas.input import PredictionInput

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    if not os.path.exists(model_path):
        return None
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception:
        return None

def predict_with_model(model, input_data: PredictionInput):
    # Adapter selon le modèle (ex: DataFrame, liste, etc.)
    features = [input_data.feature1, input_data.feature2]
    if model is None:
        raise ValueError("Aucun modèle n'est chargé.")
    prediction = model.predict([features])
    return prediction[0]

def get_model_info(model):
    # Adapter selon le modèle (type, params, etc.)
    if model is None:
        return {"error": "Aucun modèle n'est chargé."}
    return {"model_type": str(type(model)), "params": getattr(model, 'get_params', lambda: None)()}
