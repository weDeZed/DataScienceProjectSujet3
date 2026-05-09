import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Analyse des données (EDA)")

# Charger les données
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(base_dir, "dataSet", "marketing_and_sales_clean.csv")
    return pd.read_csv(file_path)

df = load_data()

# Distribution des budgets
st.header("Distribution des budgets par canal")

# On exclut "Influencer" car c'est une valeur catégorielle
channels_budget = ["TV", "Radio", "Social Media"]

# Un Box Plot (boîte à moustaches) est idéal pour voir la répartition et les valeurs aberrantes
fig_box = px.box(df, y=channels_budget, title="Répartition et dispersion des budgets")
fig_box.update_layout(xaxis_title="Canal de communication", yaxis_title="Budget Alloué en Million")
st.plotly_chart(fig_box, use_container_width=True)

# On garde toutes les colonnes pour la suite (corrélations)
channels = ["TV", "Radio", "Social Media", "Influencer"]

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
if "Influencer" in df.columns:
    # Optionnel: mapper les valeurs numériques vers des labels pour le graphique
    influencer_map = {1: "Nano", 2: "Micro", 3: "Macro", 4: "Mega"}
    df_plot = df.copy()
    df_plot["Influencer_Label"] = df_plot["Influencer"].map(influencer_map).fillna(df_plot["Influencer"])
    
    st.plotly_chart(px.pie(df_plot, names="Influencer_Label", title="Types d’influenceurs"), use_container_width=True)
else:
    st.info("Colonne 'Influencer' absente des données.")
