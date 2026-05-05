import streamlit as st
import requests

st.markdown("""
Remplissez le formulaire ci-dessous pour obtenir une prédiction de ventes selon votre budget marketing.
""")

st.title("🤖 Prédiction des ventes")
st.markdown("""
<span style='font-size:18px;'>
<b>Obtenez une estimation instantanée de vos ventes en fonction de vos budgets marketing.</b><br>
Remplissez les champs ci-dessous, puis cliquez sur <b>Prédire les ventes</b> pour voir le résultat et un graphique.
</span>
""", unsafe_allow_html=True)


st.subheader("Paramètres de votre campagne marketing")
col1, col2 = st.columns(2)
with col1:
    budget_tv = st.slider("Budget TV (€)", 0, 100000, 10000, step=1000)
    budget_radio = st.slider("Budget Radio (€)", 0, 100000, 10000, step=1000)
with col2:
    budget_social = st.slider("Budget Social Media (€)", 0, 100000, 10000, step=1000)
    type_influenceur = st.selectbox("Type d’influenceur", ["Mega", "Macro", "Micro", "Nano"])

influencer_map = {"Mega": 4, "Macro": 3, "Micro": 2, "Nano": 1}
payload = {
    "tv": budget_tv,
    "radio": budget_radio,
    "social_media": budget_social,
    "influencer": influencer_map[type_influenceur]
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

if st.button("Prédire les ventes", use_container_width=True):
    st.markdown("""
    <hr style='margin:10px 0;'>
    <b>Résumé de votre saisie :</b>
    """, unsafe_allow_html=True)
    st.write({
        "Budget TV (€)": budget_tv,
        "Budget Radio (€)": budget_radio,
        "Budget Social Media (€)": budget_social,
        "Type d’influenceur": type_influenceur
    })
    result = call_api(payload)
    if "prediction" in result:
        st.markdown("""
        <div style='background:#e3f2fd;padding:20px;border-radius:10px;margin:20px 0;'>
        <span style='font-size:22px;color:#1976d2;'><b>Prédiction de ventes estimée :</b></span><br>
        <span style='font-size:32px;color:#388e3c;'><b>{:.2f} ventes</b></span>
        </div>
        """.format(result['prediction']), unsafe_allow_html=True)
        # Graphique simple
        st.bar_chart({"Votre budget": [result['prediction']]})
    else:
        st.error(f"Erreur lors de la prédiction : {result.get('error', 'Inconnue')}")
