import streamlit as st
from setting import *

def menu():
    check = False    
    st.sidebar.page_link("app.py", label = "🏠 홈")
    st.sidebar.page_link("pages/input.py", label = "📓 민원 입력 및 출력")
    st.sidebar.page_link("pages/history.py", label = "🕛 민원 히스토리")
    st.sidebar.markdown("---") 
    if st.sidebar.button("⚙️설정"):
        setting()

    st.sidebar.markdown("---")
    #st.sidebar.page_link("pages/setting.py", label = "⚙️ 설정")
  