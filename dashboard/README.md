# Dashboard Marketing – ROI & Prédictions

## Lancer le dashboard

1. Créez un environnement virtuel python dans le dossier api :
   ```bash
   python -m venv ./dashboard
   dashboard/Scripts/activate
   ```
1. Installez les dépendances :
   ```bash
   pip install -r dashboard/requirements.txt
   ```
2. Lancez Streamlit :
   ```bash
   streamlit run dashboard/app.py
   ```

## Fonctionnalités principales
- Analyse des données (EDA)
- KPIs marketing
- Prédiction des ventes (via API)
- Simulation de budget

## Remarques
- Le dashboard fonctionne même si l’API n’est pas disponible (message d’erreur propre)
- Personnalisez les features selon votre modèle
- Ajoutez votre logo dans `assets/` si besoin
