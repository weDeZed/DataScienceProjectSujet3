from pydantic import BaseModel

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PredictionInput(BaseModel):
    tv: float
    radio: float
    social_media: float
    influencer: float  # ou int selon l'encodage
