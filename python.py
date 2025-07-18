import streamlit as st
import pandas as pd

st.title("Madlibs Game")
st.header("___ went to ____ to ___")

a=st.text_input("enter the name of a person")
b=st.text_input("enter the name of a place")
c=st.text_input("enter the name of an action")

button=st.button("done")
if button:
    st.markdown(f"{a} went to {b} to {c}")






