import streamlit as st
import requests
import numpy as np

st.title("🧪 Simulation de budget marketing")

st.markdown("""
Testez différents scénarios de budget et comparez l’impact sur les ventes attendues.
""")

# Valeurs de base
budget_tv = st.slider("Budget TV actuel", 0, 100000, 10000, step=1000)
budget_radio = st.slider("Budget Radio actuel", 0, 100000, 10000, step=1000)
budget_social = st.slider("Budget Social Media actuel", 0, 100000, 10000, step=1000)

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
    budget_tv_sim = int(budget_tv * (1 + variation/100))
    budget_radio_sim = int(budget_radio * (1 + variation/100))
    budget_social_sim = int(budget_social * (1 + variation/100))

    payload_actuel = {"feature1": budget_tv, "feature2": budget_radio}
    payload_sim = {"feature1": budget_tv_sim, "feature2": budget_radio_sim}

    res_actuel = call_api(payload_actuel)
    res_sim = call_api(payload_sim)

    ventes_actuel = res_actuel.get("prediction", 0)
    ventes_sim = res_sim.get("prediction", 0)

    st.write(f"Ventes actuelles estimées : {ventes_actuel}")
    st.write(f"Ventes simulées estimées : {ventes_sim}")

    st.bar_chart({"Actuel": [ventes_actuel], "Simulé": [ventes_sim]})
