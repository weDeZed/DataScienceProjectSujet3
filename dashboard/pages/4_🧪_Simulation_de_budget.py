import streamlit as st
import requests
import numpy as np

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


st.title("🧪 Simulation de budget marketing")

st.markdown("""
Testez différents scénarios de budget et comparez l’impact sur les ventes attendues.
""")

# Valeurs de base
budget_tv = st.slider("Budget TV actuel", 0.0, 150.0, 50.0, step=1.0)
budget_radio = st.slider("Budget Radio actuel", 0.0, 100.0, 20.0, step=1.0)
budget_social = st.slider("Budget Social Media actuel", 0.0, 50.0, 5.0, step=0.5)
type_influenceur = st.selectbox("Type d’influenceur actuel", ["Mega", "Macro", "Micro", "Nano"])

influencer_mapping = {"Nano": 1, "Micro": 2, "Macro": 3, "Mega": 4}

variation = st.slider("Variation (%)", -50, 50, 0, step=5)

# Simulation
def call_api(payload):
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json().get("detail", "Erreur API")}
    except Exception as e:
        return {"error": str(e)}

if st.button("Simuler"):
    # Budget simulé
    budget_tv_sim = max(0, budget_tv * (1 + variation/100))
    budget_radio_sim = max(0, budget_radio * (1 + variation/100))
    budget_social_sim = max(0, budget_social * (1 + variation/100))
    influencer_val = influencer_mapping[type_influenceur]

    payload_actuel = {
        "tv": budget_tv,
        "radio": budget_radio,
        "social_media": budget_social,
        "influencer": influencer_val
    }
    payload_sim = {
        "tv": budget_tv_sim,
        "radio": budget_radio_sim,
        "social_media": budget_social_sim,
        "influencer": influencer_val
    }

    res_actuel = call_api(payload_actuel)
    res_sim = call_api(payload_sim)

    ventes_actuel = res_actuel.get("prediction", 0)
    ventes_sim = res_sim.get("prediction", 0)

    st.write(f"Ventes actuelles estimées : {ventes_actuel}")
    st.write(f"Ventes simulées estimées : {ventes_sim}")

    st.bar_chart({"Actuel": [ventes_actuel], "Simulé": [ventes_sim]})
