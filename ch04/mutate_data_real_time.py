from ast import main
import streamlit as st
import pandas as pd
import random


def random_data(n):
    y = [random.randint(1, n) for value in range(n)]
    return y


if __name__ == "__main__":
    df1 = pd.DataFrame(data={"y": [1, 2]})
    col1, col2 = st.columns([1, 3])
    with col1:
        table = st.table(df1)
    with col2:
        chart = st.line_chart(df1)
        n = st.number_input("Number of rows to add", 0, 10, 1)
    if st.button("Update"):
        y = random_data(n)
        df2 = pd.DataFrame(data={"y": y})
        table.add_rows(df2)
        chart.add_rows(df2)
