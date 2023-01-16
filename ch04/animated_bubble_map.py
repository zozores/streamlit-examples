import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("datasets/gdp-per-capita-worldbank.csv").sort_values(
    by=["Year", "Entity"]
)
fig = px.scatter_geo(
    df,
    locations=df["Code"],
    color=df["GDP per capita, PPP (constant 2017 international $)"],
    hover_name=df["Entity"],
    size=df["GDP per capita, PPP (constant 2017 international $)"],
    animation_frame=df["Year"],
    color_continuous_scale="Hot",
)
st.title("Animated Bubble Map")
st.write(fig)
