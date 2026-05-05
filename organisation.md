
DataScienceProjectSujet3/
│
├── data/                     # Dataset brut + dataset nettoyé
│   ├── raw/
│   └── processed/
│
├── notebooks/                # EDA, tests, prototypes
│   ├── 01_eda/
│   ├── 02_feature_engineering/
│   └── 03_model_prototypes/
│
├── ml_models/                # Travail du ML Engineer
│   ├── training/             # Scripts d'entraînement
│   ├── evaluation/           # Comparaison des modèles
│   └── saved_models/         # Modèles .pkl finaux
│
├── api/                      # Travail du Data Engineer
│   ├── app.py                # FastAPI/Flask
│   ├── requirements.txt
│   └── utils/
│
├── dashboard/                # Travail du Product Designer
│   ├── app.py                # Streamlit/Dash
│   ├── pages/
│   └── assets/
│
├── docs/                     # Rapport + Présentation
│   ├── rapport/
│   └── slides/
│
├── tests/                    # Tests unitaires
│
├── README.md
└── .gitignore
