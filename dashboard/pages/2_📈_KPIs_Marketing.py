import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📈 KPIs Marketing")

@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(base_dir, "dataSet", "marketing_and_sales_clean.csv")
    return pd.read_csv(file_path)

df = load_data()
channels = ["TV", "Radio", "Social Media", "Influencer"]

# KPIs
st.header("KPIs principaux")

# Calculs (en excluant la variable catégorielle "Influencer" des totaux monétaires)
channels_budget = ["TV", "Radio", "Social Media"]
total_budget = df[channels_budget].sum().sum()
mean_budget = df[channels_budget].mean().mean()
mean_sales = df['Sales'].mean()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Budget total investi", f"{total_budget:,.1f} M€")
with col2:
    st.metric("Budget moyen par canal", f"{mean_budget:,.1f} M€")
with col3:
    st.metric("Ventes moyennes", f"{mean_sales:,.1f} M")

if "ROI" in df.columns:
    st.metric("ROI moyen", f"{df['ROI'].mean():.2f}")

# Top 3 canaux les plus corrélés aux ventes
corrs = df[channels + ["Sales"]].corr()["Sales"].abs().sort_values(ascending=False)
top3 = corrs.drop("Sales").head(3)
st.subheader("Top 3 canaux les plus corrélés aux ventes")
st.write(top3)

# Répartition du budget par canal
st.subheader("Répartition du budget par canal")
st.plotly_chart(px.pie(values=df[channels].sum(), names=channels, title="Répartition du budget"), use_container_width=True)

# Bar chart : importance des variables (feature importance)
if "feature_importance" in df.columns:
    st.subheader("Importance des variables")
    st.bar_chart(df["feature_importance"])

# Line chart : évolution des ventes
if "Date" in df.columns:
    st.subheader("Évolution des ventes")
    st.line_chart(df.set_index("Date")["Sales"])
