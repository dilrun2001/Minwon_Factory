import streamlit as st
from datetime import datetime

#from menu import menu

#st.set_page_config(page_title = "설정", page_icon = "⚙️", layout = "wide")
#menu()
check = False
def setting():
     llm_model = st.sidebar.selectbox(
     "LLM 모델 선택", ("gemma3:latest", "llama3:latest"), index = 0
     )

     if llm_model == "heegyu/EEVE-Korean-Instruct-10.8B-v1.0-GGUF":
          st.session_state.llm_model = "heegyu/EEVE-Korean-Instruct-10.8B-v1.0-GGUF"
     else:
          st.session_state.llm_model = "lmstudio-community/gemma-2-9b-it-GGUF"


     name = st.sidebar.text_input(
          "이름을 입력하세요.",
          placeholder = "이름"
     )


     department = st.sidebar.text_input("부서명을 입력헤주세요.", placeholder =  "부서명")
     tel = st.sidebar.text_input(""
     "담당자 행정 전화번호를 입력하세요.", placeholder="051-200-0000"
     )


     if st.sidebar.button("설정 저장"):
          st.session_state.name = name
          st.session_state.department = department
          st.session_state.tel = tel
          st.session_state.llm_model = llm_model
          st.success(f"설정이 저장되었습니다.     \nLLM 모델 : {llm_model}    \n담당자 번호 : {tel}      \n부서명 : {department}")

def setting_erase():
     with st.sidebar:
          st.sidebar.write("")