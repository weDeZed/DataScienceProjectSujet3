import streamlit as st
import requests

st.title("🤖 Prédiction des ventes")

st.markdown("""
Remplissez le formulaire ci-dessous pour obtenir une prédiction de ventes selon votre budget marketing.
""")

# Formulaire
budget_tv = st.number_input("Budget TV", min_value=0.0, max_value=150.0, value=50.0, step=1.0)
budget_radio = st.number_input("Budget Radio", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
budget_social = st.number_input("Budget Social Media", min_value=0.0, max_value=50.0, value=5.0, step=0.5)
type_influenceur = st.selectbox("Type d’influenceur", ["Mega", "Macro", "Micro", "Nano"])

influencer_mapping = {
    "Nano": 1,
    "Micro": 2,
    "Macro": 3,
    "Mega": 4
}

payload = {
    "tv": budget_tv,
    "radio": budget_radio,
    "social_media": budget_social,
    "influencer": influencer_mapping[type_influenceur]
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
