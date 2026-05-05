import pickle
import os
from api.schemas.input import PredictionInput

def load_model():
    model_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', 'ml_models', 'saved_models', 'gradient_boosting', 'model.pkl'))
    # DataScienceProjectSujet3\ml_models\saved_models\gradient_boosting

    if not os.path.exists(model_path):
        return None
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception:
        return None

def predict_with_model(model, input_data: PredictionInput):
    if model is None:
        raise ValueError("Aucun modèle n'est chargé.")
    # Adapter selon le modèle (ex: DataFrame, liste, etc.)
    features = [
        input_data.tv,
        input_data.radio,
        input_data.social_media,
        input_data.influencer
    ]
    prediction = model.predict([features])
    return float(prediction[0])

def get_model_info(model):
    # Adapter selon le modèle (type, params, etc.)
    if model is None:
        return {"error": "Aucun modèle n'est chargé."}
    return {"model_type": str(type(model)), "params": getattr(model, 'get_params', lambda: None)()}
