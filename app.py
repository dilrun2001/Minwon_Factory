import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pandas as pd
from datetime import datetime
from menu import menu


st.set_page_config(page_title = "새올민원자동답변기", page_icon="📝", layout="wide")

st.title("📝 민원 응답 생성기")

#도움말, 프로그램 개요 등 입력 파트
st.markdown("""
## 폰트 설치하기 (필수)

- 프로그램 폴더 내 title_ttf 폴더에서 Giants-Regular.ttf, NEXON Kart Gothic ExtraBold.ttf 설치
- 프로그램 실행 시 아래 이미지와 같은 폰트가 나와야 정상입니다.

 엑셀 파일 설명

- 예시 파일 마크2 폴더에서 예시 파일을 확인해주세요.
- 이때, 팀장의 정보는 아래쪽에 무조건 정렬 시켜주세요.
- 하이라이트가 없는 경매자는 x, 혹은 공백으로 처리해주세요.
- 지원하는 파일 양식 : xlsx, csv



## 프로그램 최초 설정

- 사운드 : BGM 0%, Effect 50%
- 경매 : 1번 설정, 넥스트 ON, 팀장 소개 ON, 자동 모드 OFF
- 해상도 : 1920 x 1080 고정, 전체 화면, 창 크기 조절 불가

## 경매 초기 설정

- 왼쪽 위부터 설정 선택 - 게임 선택 - 넥스트 ON/OFF - 팀장 소개 ON/OFF - 자동 모드 ON/OFF - 파일 입력
- Game Select에서 게임 선택 → 파일 입력 시 NEXT 버튼 생성
- 이때 파일 입력이 끝난 이후 경매 기초 설정, 게임 선택을 바꿀 수 없습니다.(아래 이미지 참조)



## 경매자/팀장 하이라이트

- 하이라이트 출력 방식 : 웹브라우저 링크를 불러오는 방식
- 원할한 진행을 위해 유튜브와 같은 플랫폼을 권장합니다.

## 낙찰자 팀장 선택

- 기본적으로 경매자 낙찰 시 아래와 같은 팝업창이 출력됩니다.
- 혹시나 실수로 창을 껐을 경우에는 s키를 누르면 다시 팝업창이 출력됩니다.
- 혹은 설정 → 경매 설정 → 낙찰자 팀장 선택 항목을 누르시면 동일한 팝업창이 출력됩니다.
- 낙찰자의 팀장을 선택하지 않으면 경매는 다음 단계로 진행되지 않습니다.



## 경매 일시정지/정지

- 경매 시작 시 볼륨/설정 버튼이 아래 이미지와 같이 변경됩니다.
- 일시정지: 아래 이미지 버튼 누르면 일시 정지 (이때, 타이머는 일시 정지 된 순간에 정지)
- 정지 : 정지 버튼 3번 눌러야 경매가 정지됩니다.



## Config 파일 관련

- config.yml, file_config.yml은 절대 삭제하시면 안됩니다.
- yml 파일은 메모장으로도 열기 및 편집이 가능합니다.

### config.yml

- config.yml은 프로그램의 일부 설정을 변경할 수 있습니다.
- Developer Mode 항목은 Image 항목을 제외하고 암호가 없으면 사용할 수 없습니다.
- 각 게임 경매의 색상은 기존 입력된 값을 참고해주세요.



### file_config.yml

- file_config.yml은 이미지, 사운드 파일의 경로를 수정할 수 있습니다.
- 이때, 이미지 or 사운드 파일을 교체했을 경우 해당 파일에서 경로를 꼭 수정해주셔야 합니다.
- 경로 미수정 시 프로그램이 경매를 진행하지 않고, 다음 화면으로 넘어가지 않습니다.



- 이미지 파일 지원 확장자 : png
- 사운드 파일 지원 확장자 : mp3, wav, ogg



## 프로그램 단축키

- F1 : 도움말
- F5 : 경매 시작
- F7 : 효과음 음소거 전환
- F8 : BGM 음소거 전환
- Q : 경매 빠른 입찰
- S : 낙찰자 팀장 선택 창
- P : 경매 일시 정지

---

## CREDIT

동아대학교 Game Crew GND Auction

Project Manager : 조중현
Developer : 조중현
UI/UX Designer : 김민경, 조중현

Resource Assistant : 김민경, 동민경, 조중현
Program Maintenance : 조중현
Manual Editor: 김민경, 조중현

프로그램에 대한 피드백, 버그 제보는 디스코드 junghyeon9363으로 말씀해주세요.

(본 프로그램 코드 및 배포 권한은 개발자에게 있습니다.)""")


#현재 준비된 세팅이 없는 관계로 임시 처리
if "department" not in st.session_state:
    st.session_state.department = ""
if "name" not in st.session_state:
    st.session_state.name = ""
if "tel" not in st.session_state:
    st.session_state.tel = ""
if "llm_model" not in st.session_state:
    st.session_state.llm_model = "llama3:latest"
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
if "main" not in st.session_state:
    st.session_state.main = None

menu()