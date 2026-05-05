from pydantic import BaseModel

class PredictionInput(BaseModel):
    tv: float
    radio: float
    social_media: float
    influencer: float  # ou int selon l'encodage
