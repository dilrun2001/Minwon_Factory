import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pandas as pd
from datetime import datetime
from menu import menu

st.set_page_config(page_title = "민원히스토리", layout = "wide")
#history_df = st.session_state.df
menu()
if not st.session_state.df.empty:
    st.dataframe(st.session_state.df)
    st.button("")
else:
    st.info("아직 생성된 답변이 없습니다.")

