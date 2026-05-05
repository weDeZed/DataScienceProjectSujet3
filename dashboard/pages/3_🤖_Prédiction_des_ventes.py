import streamlit as st
import requests

st.title("🤖 Prédiction des ventes")

st.markdown("""
Remplissez le formulaire ci-dessous pour obtenir une prédiction de ventes selon votre budget marketing.
""")

# Formulaire
budget_tv = st.slider("Budget TV", 0, 100000, 10000, step=1000)
budget_radio = st.slider("Budget Radio", 0, 100000, 10000, step=1000)
budget_social = st.slider("Budget Social Media", 0, 100000, 10000, step=1000)
type_influenceur = st.selectbox("Type d’influenceur", ["Mega", "Macro", "Micro", "Nano"])

payload = {
    "feature1": budget_tv,
    "feature2": budget_radio
    # Ajouter les autres features selon le modèle
}

def call_api(payload):
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json().get("detail", "Erreur API")}
    except Exception as e:
        return {"error": str(e)}

if st.button("Prédire les ventes"):
    result = call_api(payload)
    if "prediction" in result:
        st.success(f"Avec ce budget, vous pouvez espérer environ {result['prediction']} ventes.")
    else:
        st.error(f"Erreur lors de la prédiction : {result.get('error', 'Inconnue')}")
