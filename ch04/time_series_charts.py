import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = np.random.randn(40, 2)
df = pd.DataFrame(data, columns=["Column 1", "Column 2"])
df.index = pd.date_range(start="1/1/2018", end="2/9/2018", freq="D")

fig = px.line(df, x=df.index, y=df.columns)
st.title("Time-Series Charts")
st.write(fig)
