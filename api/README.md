# 📦 API FastAPI – Prédiction Marketing

## 🚀 Présentation
Cette API permet de réaliser des prédictions de ventes à partir de budgets marketing (TV, Radio, Social Media, Influenceur) grâce à un modèle de machine learning entraîné.

---

## 📂 Structure du dossier
```
api/
│── app.py                # Point d'entrée FastAPI
│── models/
│     └── model.pkl       # Modèle ML entraîné (pickle)
│── schemas/
│     └── input.py        # Schéma Pydantic pour la validation des entrées
│── utils/
│     └── loader.py       # Fonctions de chargement et prédiction du modèle
│── README.md             # Documentation de l'API
```

---

## ⚙️ Installation & Lancement

1. Installez les dépendances :
   ```bash
   pip install fastapi uvicorn pydantic
   ```
2. Placez le modèle entraîné dans `api/models/model.pkl`.
3. Lancez l’API :
   ```bash
   uvicorn api.app:app --reload
   ```
4. Accédez à la documentation interactive :
   - Swagger UI : [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc : [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛣️ Endpoints disponibles

### `GET /health`
- **Description** : Vérifie que l’API est opérationnelle.
- **Réponse** : `{ "status": "ok" }`

### `GET /model-info`
- **Description** : Retourne des informations sur le modèle ML chargé.
- **Réponse** :
  - Succès : `{ "model_type": "...", "params": {...} }`
  - Erreur : `503` si aucun modèle n’est chargé

### `POST /predict`
- **Description** : Prédit les ventes à partir des budgets fournis.
- **Entrée (JSON)** :
  ```json
  {
    "tv": 10000,
    "radio": 5000,
    "social_media": 8000,
    "influencer": 2
  }
  ```
  *(adapter les clés selon le schéma réel)*
- **Réponse** :
  - Succès : `{ "prediction": 123.45 }`
  - Erreur : `503` si le modèle n’est pas chargé, `400` si les données sont invalides

---

## 📝 Exemple d’appel avec `requests`
```python
import requests
payload = {
    "tv": 10000,
    "radio": 5000,
    "social_media": 8000,
    "influencer": 2
}
res = requests.post("http://localhost:8000/predict", json=payload)
print(res.json())
```

---

## 🛠️ Personnalisation
- **Modèle** : Remplacez `model.pkl` par votre propre modèle entraîné (mêmes features).
- **Schéma d’entrée** : Modifiez `schemas/input.py` pour refléter les noms et types attendus.
- **Logique de prédiction** : Adaptez `utils/loader.py` si le modèle ou le prétraitement change.

---

## ❓ FAQ
- **Que faire si l’API retourne "Aucun modèle n'est chargé" ?**
  - Vérifiez que `model.pkl` existe et est un vrai fichier pickle.
- **Comment ajouter de nouveaux endpoints ?**
  - Ajoutez-les dans `app.py` en suivant la structure FastAPI.
- **Comment tester l’API ?**
  - Utilisez Swagger UI ou des outils comme Postman/curl/requests.

---

## 👨‍💻 Auteur
- Projet Data Science EFREI – 2026
