import streamlit as st
import pandas as pd
import numpy as np
import time


@st.cache
def dataframe(rows):
    df = pd.DataFrame(
        np.random.randn(rows, 5), columns=("col %d" % i for i in range(5))
    )


runtime = pd.DataFrame(
    data={
        "Number of rows": [10, 100, 1000, 10000, 100000, 1000000, 10000000],
        "First runtime (s)": None,
        "Second runtime (s)": None,
        "Runtime saved (%)": None,
    }
)

st.write(runtime)
st.write(len(runtime))

for i in range(0, len(runtime)):
    start = time.time()
    dataframe(runtime.loc[i]["Number of rows"])
    stop = time.time()
    runtime.loc[i, "First runtime (s)"] = stop - start

    start = time.time()
    dataframe(runtime.loc[i]["Number of rows"])
    stop = time.time()
    runtime.loc[i, "Second runtime (s)"] = stop - start

    runtime.loc[i, "Runtime saved (%)"] = 100 - int(
        100
        * (runtime.loc[i, "Second runtime (s)"] / runtime.loc[i, "First runtime (s)"])
    )

st.write(runtime)
