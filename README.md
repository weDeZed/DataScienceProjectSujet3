# Système de Prédiction des Ventes Marketing

Projet de Machine Learning end-to-end pour la prédiction du chiffre d'affaires à partir des budgets publicitaires multi-canaux (TV, Radio, Social Media, Influenceurs).

---

## Objectif

Permettre aux équipes marketing de :
- **Prédire les ventes** en fonction d'une allocation budgétaire sur 4 canaux
- **Simuler différents scénarios** pour optimiser les 
  
---

## Structure du projet

```
TP FINAL/
├── dataSet/
│   ├── marketing_and_sales.csv              # Dataset brut (4 572 enregistrements)
│   ├── marketing_and_sales_clean.csv        # Dataset nettoyé (4 546 enregistrements)
│   ├── cleanDataSet.py                      # Script de nettoyage
│   ├── correlation_dataset.ipynb            # EDA & analyse des corrélations
│   └── audit_preparation_donnees.md         # Rapport d'audit qualité des données
│
├── ml_models/
│   ├── training/                            # Notebooks d'entraînement
│   │   ├── linear_regression.ipynb
│   │   ├── polynomial_linear_regression.ipynb
│   │   ├── elasticnet_regression.ipynb
│   │   ├── gradient_boosting.ipynb
│   │   ├── random_forest_regressor.ipynb
│   │   └── mlp_regressor.ipynb
│   └── saved_models/                        # Modèles sérialisés & métriques
│       ├── linear_regression/               # Modèle retenu
│       ├── elasticnet_regression/
│       ├── polynomial_linear_regression/
│       ├── mlp_regressor/
│       ├── gradient_boosting/
│       ├── random_forest_regressor/
│
├── api/                                     # Service FastAPI
│   ├── app.py
│   ├── schemas/input.py
│   ├── utils/loader.py
│   └── requirements.txt
│
├── dashboard/                               # Interface Streamlit
│   ├── app.py
│   ├── pages/
│   │   ├── 1_📊_Analyse_des_données.py
│   │   ├── 2_📈_KPIs_Marketing.py
│   │   ├── 3_🤖_Prédiction_des_ventes.py
│   │   ├── 4_🧪_Simulation_de_budget.py
│   └── requirements.txt
│
└── model_comparison.ipynb                   # Comparaison automatisée des modèles
```

---

## Dataset

| Attribut | Description | Plage |
|---|---|---|
| **TV** | Budget publicitaire TV (M€) | 10 – 100 |
| **Radio** | Budget publicitaire Radio (M€) | 0 – 49 |
| **Social Media** | Budget Social Media (M€) | 0 – 14 |
| **Influencer** | Catégorie d'influenceur (Nano/Micro/Macro/Mega) | 1 – 4 |
| **Sales** | Chiffre d'affaires (M€) — cible | 31 – 364 |

- **4 572 enregistrements** bruts → **4 546** après nettoyage (26 lignes supprimées pour valeurs manquantes)
- Encodage ordinal des influenceurs : Nano=1, Micro=2, Macro=3, Mega=4
- Multicolinéarité TV-Radio détectée (VIF TV=19.97, VIF Radio=21.14)

---

## Modèles entraînés & comparaison

| Modèle | R² | RMSE | MAE | Statut |
|---|---|---|---|---|
| **Régression Linéaire** | **0.9989** | **2.99** | **2.38** | Retenu |
| Polynomial | 0.9990 | 3.00 | 2.39 | — |
| ElasticNet | 0.9990 | 3.00 | 2.39 | — |
| MLP (réseau de neurones) | 0.9990 | 3.03 | 2.41 | — |
| Gradient Boosting | 0.9989 | 3.05 | 2.43 | — |
| Random Forest | 0.9981 | 4.08 | 3.04 | — |

**Modèle retenu : Régression Linéaire**
- Performance équivalente aux modèles plus complexes
- Interprétabilité maximale (coefficients explicites + SHAP)
- La TV est le levier dominant (coefficient ~3.56×)
- Validation croisée 5-fold confirmée

---

## Architecture

```
Dashboard Streamlit  ──►  API FastAPI  ──►  linear_regression.pkl (ventes)
                                       ──►  random_forest.pkl    (ROI)
```

### API FastAPI

| Endpoint | Méthode | Description |
|---|---|---|
| `/health` | GET | Statut du service |
| `/model-info` | GET | Métadonnées du modèle actif |
| `/predict` | POST | Prédiction des ventes |

**Exemple de requête `/predict` :**
```json
{
  "tv": 200.0,
  "radio": 25.0,
  "social_media": 8.5,
  "influencer": 3
}
```

### Dashboard Streamlit (5 pages)

| Page | Contenu |
|---|---|
| Analyse des données | EDA, heatmap, distributions, scatter plots |
| KPIs Marketing | Métriques de performance et efficacité par canal |
| Prédiction des ventes | Interface de prédiction en temps réel |
| Simulation de budget | Analyse de sensibilité et optimisation |

---

## Lancement

### 1. Installer les dépendances

Pour lancer l'API et le dashboard, suivre la procédure des README.md de ces différents dossiers.

---

## Interprétabilité

Les analyses SHAP sont disponibles dans [ml_models/saved_models/linear_regression/](ml_models/saved_models/linear_regression/) :
- `shap_summary.png` — Importance et direction de chaque feature
- `shap_bar.png` — Importance absolue moyenne
- `feature_importance.png` — Importance relative des variables

---

## Technologies

- **Python** 3.x
- **scikit-learn** — Entraînement des modèles
- **FastAPI + Uvicorn** — API REST
- **Streamlit** — Dashboard interactif
- **SHAP** — Interprétabilité des modèles
- **pandas / numpy / matplotlib / seaborn** — Data processing & visualisation
