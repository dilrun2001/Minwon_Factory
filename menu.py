import streamlit as st



#사이드바 페이지 이동 버튼 함수
def menu():

    st.sidebar.subheader("페이지 이동")
    st.sidebar.page_link("app.py", label = "🏠 홈")
    st.sidebar.page_link("pages/input.py", label = "📓 민원 입력 및 출력")
    st.sidebar.page_link("pages/history.py", label = "🕛 민원 히스토리")
    st.sidebar.page_link("pages/settingpage.py", label = "⚙️ 설정")
    st.sidebar.markdown("---") 
  