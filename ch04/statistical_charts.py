import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = np.random.randn(40, 2)
df = pd.DataFrame(data, columns=["Column 1", "Column 2"])

# Histogram
fig = go.Figure()
fig.add_trace(go.Histogram(name="Column 1", x=df["Column 1"]))
fig.add_trace(go.Histogram(name="Column 2", x=df["Column 2"]))
fig.update_layout(barmode="overlay")
fig.update_traces(opacity=0.75)
st.title("Histogram")
st.write(fig)

# Box Plot
fig = go.Figure()
fig.add_trace(go.Box(y=df["Column 1"], name="Column 1", boxmean="sd"))
fig.add_trace(go.Box(y=df["Column 2"], name="Column 2", boxmean="sd"))
st.title("Box Plot")
st.write(fig)
