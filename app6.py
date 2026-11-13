import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0
    
if st.button("더하기"):
    st.session_state.count += 1
    
if st.button("처음으로"):
    st.session_state.count = 0
    
st.write(f"클릭횟수: {st.session_state.count}")

with st.form("bmi_form"):
    height = st.number_input("키(cm)", 100.0, 220.0, 170.0)
    weight = st.number_input("몸무게(kg)", 30.0, 200.0, 65.0)
    done = st.form_submit_button("계산하기")

if done:
    bmi = weight / (height / 100) ** 2
    st.write(f"BMI: {bmi:.1f}")