import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(0)

df = pd.DataFrame(np.random.randn(12, 3), columns=("Score 1", "Score 2", "Score 3"))
df["Name"] = pd.DataFrame(
    [
        "John",
        "Alex",
        "Jessica",
        "John",
        "Alex",
        "John",
        "Jessica",
        "John",
        "Alex",
        "Alex",
        "Jessica",
        "Jessica",
    ]
)
df["Category"] = pd.DataFrame(
    ["B", "A", "D", "C", "C", "A", "B", "C", "B", "A", "A", "D"]
)
st.subheader("Original Dataframe")
st.write(df)

df = df.groupby(["Name", "Category"]).first()
st.subheader("Mutated Dataframe")
st.write(df)
