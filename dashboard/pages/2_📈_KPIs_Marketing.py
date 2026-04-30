import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 KPIs Marketing")

@st.cache_data
def load_data():
    return pd.read_csv("../marketing_and_sales_clean.csv")

df = load_data()
channels = ["TV", "Radio", "Social Media", "Influencer"]

# KPIs
st.header("KPIs principaux")
st.metric("Budget total investi", f"{df[channels].sum().sum():,.0f} €")
st.metric("Budget moyen par canal", f"{df[channels].mean().mean():,.0f} €")
st.metric("Ventes moyennes", f"{df['Sales'].mean():.0f}")
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
