
import streamlit as st
import pandas as pd

DATA = "heart_failure_clinical_records_dataset.csv"
df = pd.read_csv(DATA)

with st.sidebar:
    st.header("필터")
    low, high = st.slider("나이 범위", 40, 95, (40, 95))

part = df[(df["age"] >= low) & (df["age"] <= high)]

st.title("심부전 환자 조회")
st.write(f"선택한 환자: {len(part)}명")

c1, c2, c3 = st.columns(3)
c1.metric("환자 수", f"{len(part)}명")
c2.metric("평균 나이", f"{part['age'].mean():.1f}세")
c3.metric("사망 비율", f"{part['DEATH_EVENT'].mean() * 100:.1f}%")

tab1, tab2 = st.tabs(["표", "요약"])
with tab1:
    st.dataframe(part, width="stretch")
with tab2:
    st.write(part[["age", "ejection_fraction"]].describe())

with st.expander("변수 설명 보기"):
    st.write("ejection_fraction: 박출률(%)")
