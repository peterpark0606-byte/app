import streamlit as st

import pandas as pd

DATA=r"C:\Users\asia\Downloads\heart_failure_clinical_records_dataset.csv"

st.title("환자 조회")
age = st.slider("나이", 40, 95, 60)
st.write(f"선택한 나이: {age}")

sex = st.selectbox("성별", ["전체", "남성", "여성"])
items = st.multiselect("함께 볼 질환",
["빈혈", "당뇨", "고혈압"],
default=["고혈압"])
st.write(f"성별: {sex}")
st.write("질환:", ", ".join(items))

view = st.radio("보기 방식", ["표", "요약"], horizontal=True)
smoker = st.checkbox("흡연자만 보기")
st.write(f"보기 방식: {view}")
st.write(f"흡연자만: {smoker}")

clicked = st.button("인사하기")
st.write(f"버튼 값: {clicked}")
if clicked:
    st.success("안녕하세요!")
    
df = pd.read_csv(DATA)
low, high = st.slider("나이범위", 40, 95, (60, 80))
part = df[(df["age"] >= low) & (df["age"] <= high)]

st.write(f"{low}~{high}세환자: {len(part)}명")
st.dataframe(part, width="stretch")