import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Analyse des données (EDA)")

# Charger les données
@st.cache_data
def load_data():
    return pd.read_csv("../marketing_and_sales_clean.csv")

df = load_data()

# Distribution des budgets
st.header("Distribution des budgets par canal")
channels = ["TV", "Radio", "Social Media", "Influenceurs"]
st.bar_chart(df[channels])

# Corrélation entre budgets et ventes
st.header("Corrélation budgets vs ventes")
corrs = df[channels + ["Sales"]].corr()
st.dataframe(corrs)

# Heatmap des corrélations
st.header("Heatmap des corrélations")
fig = px.imshow(corrs, text_auto=True, color_continuous_scale="Blues")
st.plotly_chart(fig, use_container_width=True)

# Scatter plots
st.header("Scatter plots : Budget vs Ventes")
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(px.scatter(df, x="TV", y="Sales", title="TV vs Sales"), use_container_width=True)
with col2:
    st.plotly_chart(px.scatter(df, x="Radio", y="Sales", title="Radio vs Sales"), use_container_width=True)
with col3:
    st.plotly_chart(px.scatter(df, x="Social Media", y="Sales", title="Social Media vs Sales"), use_container_width=True)

# Répartition des types d’influenceurs
st.header("Répartition des types d’influenceurs")
if "Influenceur_Type" in df.columns:
    st.plotly_chart(px.pie(df, names="Influenceur_Type", title="Types d’influenceurs"), use_container_width=True)
else:
    st.info("Colonne 'Influenceur_Type' absente des données.")
