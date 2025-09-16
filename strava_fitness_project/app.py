import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("strava_cleaned.csv")

st.title("🏃 Strava Fitness Dashboard")

fig1 = px.histogram(df, x="activity_type", title="Activity Distribution")
st.plotly_chart(fig1)

fig2 = px.scatter(df, x="distance_km", y="calories", color="activity_type",
                  hover_data=["duration_min"], title="Calories vs Distance")
st.plotly_chart(fig2)

fig3 = px.histogram(df, x="hour", nbins=24, title="Workout by Hour")
st.plotly_chart(fig3)
