import streamlit as st

#1차적으로는 py 파일에 필요한 부분만 css 임시 적용
#이후 필요에 따라서는 css 파일로 건드리는 방식으로 진행 고려중중
#css 파일 작업시 참고 링크 https://github.com/microsoft/Streamlit_UI_Template/tree/main


def Apply_Global_Style():
    # stToolbar = 우측 상단 툴바 (Deploy)
    # stSidebar = 사이드바
    st.markdown(
        '''
        <style>
        [data-testid = "stToolbar"]{display: none !important;} 
        [data-testid = "stSidebar"]{width: 300px !important;}
        </style>
        ''', unsafe_allow_html=True
    )

# 슬라이더 색상 css
def Apply_Slidebar_Style():
    st.markdown(
        '''
        <style>
        [role = "slider"]{background-color: #DFE5EE !important;}
        [data-testid = "stSliderThumbValue"]{color: #DFE5EE !important;}
        </style>
        ''', unsafe_allow_html=True
    )

#헤더 옆 링크 연결 부분 비활성화
def Apply_Header_Deactive():
    st.markdown(
        '''
        <style>
        [data-testid = "stHeaderActionElements"]{display: none !important;}

    ''', unsafe_allow_html=True
    )