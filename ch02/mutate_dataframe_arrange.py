import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(0)

df = pd.DataFrame(np.random.randn(4, 3), columns=("Col 1", "Col 2", "Col 3"))
st.subheader("Original Dataframe")
st.write(df)

df = df.sort_values(by="Col 1", ascending=True)
st.subheader("Mutated Dataframe")
st.write(df)
