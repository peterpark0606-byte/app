import streamlit as st
import pandas as pd

DATA = r"C:\Users\asia\Desktop\panda\healthcare-dataset-stroke-data.csv"
df=pd.read_csv(DATA)

st.title("심부전환자차트")
counts = df["DEATH_EVENT"].map({0: "생존", 1: "사망"}).value_counts()
st.bar_chart(counts)