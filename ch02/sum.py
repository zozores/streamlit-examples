import streamlit as st


def calculate_sum(n1, n2):
    return n1 + n2


st.title("Soma")
n1 = st.number_input("n1")
n2 = st.number_input("n2")

if st.button("Calcular"):
    st.write(f"A soma é: {calculate_sum(n1, n2)}")
