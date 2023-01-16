import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = np.random.randint(0, 10, size=(40, 2))
df = pd.DataFrame(data, columns=["Column 1", "Column 2"])

st.title("Dataframe")
st.write(df)

# Line Chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df["Column 1"], mode="lines", name="Column 1"))
fig.add_trace(go.Scatter(x=df.index, y=df["Column 2"], mode="lines", name="Column 2"))
st.title("Line Chart")
st.write(fig)

# Scatter Chart
fig = go.Figure(
    data=go.Scatter(
        y=df["Column 1"],
        mode="markers",
        marker=dict(
            size=10, color=df["Column 2"], colorscale="Viridis", showscale=True
        ),
    )
)
st.title("Scatter Chart")
st.write(fig)

# Bar Chart
fig = go.Figure(
    data=[
        go.Bar(name="Column 1", x=df.index, y=df["Column 1"]),
        go.Bar(name="Column 2", x=df.index, y=df["Column 2"]),
    ]
)
st.title("Bar Chart")
st.write(fig)

# Pie Chart
fig = px.pie(df, values=df.sum(), names=df.columns)
st.title("Pie Chart")
st.write(fig)

# Bar Chart - Update Layout
fig = go.Figure(
    data=[
        go.Bar(name="Column 1", x=df.index, y=df["Column 1"]),
        go.Bar(name="Column 2", x=df.index, y=df["Column 2"]),
    ]
)
fig.update_layout(
    title="Column 1 vs Index",
    xaxis_title="Index",
    yaxis_title="Value",
    legend_title="Columns",
    font=dict(family="Arial", size=10, color="black"),
)
st.title("Bar Chart - Update Layout")
st.write(fig)
