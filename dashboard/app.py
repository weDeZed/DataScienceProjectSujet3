import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Dashboard Marketing – ROI & Prédictions",
    page_icon="📈",
    layout="wide"
)

# Logo optionnel
def show_logo():
    logo_path = Path("dashboard/assets/logo.png")
    if logo_path.exists():
        st.image(str(logo_path), width=120)

show_logo()

st.title("📈 Dashboard Marketing – ROI & Prédictions")
st.markdown("""
Bienvenue sur le dashboard interactif du projet Data Science Marketing.

**Objectifs :**
- Optimiser le ROI marketing
- Analyser les canaux d’acquisition
- Prédire les ventes
- Simuler des budgets

Utilisez le menu à gauche pour naviguer entre les analyses, KPIs, prédictions et simulations.
""")

st.info("""
Ce dashboard est destiné aux responsables marketing souhaitant piloter et optimiser leurs investissements.
""")
