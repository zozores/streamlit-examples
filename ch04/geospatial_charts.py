import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("datasets/gdp-per-capita-worldbank.csv").sort_values(
    by="Year", ascending=False
)
fig = px.choropleth(
    df,
    locations=df["Code"],
    color=df["GDP per capita, PPP (constant 2017 international $)"],
    hover_name=df["Entity"],
    color_continuous_scale="Earth",
)
st.title("Geospatial Charts")
st.write(fig)
