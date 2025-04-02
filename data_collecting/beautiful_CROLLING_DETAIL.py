import re
import json
import requests
from bs4 import BeautifulSoup


##bs 4 기반으로 데이터를 질의 응답 부분을 가져오게 처리 하는 부분입니다 .


# 🔗 목록 조회 URL
list_url = "https://eminwon.saha.go.kr/emwp/gov/mogaha/ntis/web/emwp/cns/action/EmwpCnslWebAction.do"

# 📌 요청 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded",
}

# ✅ 전체 결과 저장용 리스트
tinyllama_data = []

# ✅ 페이지 반복 얼마나 진행할지 작성

#데이터 디버깅 용
for page in range(1, 276): # 2025 까지의 데이터 합습 해야 한다.
    print(f"📄 페이지 {page} 처리 중...")

    list_data = {
        "method": "selectCnslWebPage",
        "menu_id": "EMWPCnslWebInqL",
        "jndinm": "EmwpCnslWebEJB",
        "methodnm": "selectCnslWebPage",
        "context": "NTIS",
        "pageIndex": str(page),
        "pageSize": "20"
    }

    # 오류 발생시 처리 방법
    response = requests.post(list_url, data=list_data, headers=headers)
    if response.status_code != 200:
        print(f"❌ 페이지 {page} 요청 실패!")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("table.table tbody tr")

    if not rows:
        print("⛔ 더 이상 데이터 없음! 중단합니다.")
        break

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            title = cols[1].text.strip()
            onclick = cols[1].find("a")["href"]
            match = re.search(r"fncViewDtl\('(\d+)'", onclick)
            if match:
                cnsl_qna_no = match.group(1)

                detail_data = {
                    "method": "selectCnslWebShow",
                    "jndinm": "EmwpCnslWebEJB",
                    "methodnm": "selectCnslWebShow",
                    "context": "NTIS",
                    "cnsl_qna_no": cnsl_qna_no,
                }

                detail_resp = requests.post(list_url, data=detail_data, headers=headers)
                if detail_resp.status_code == 200:
                    detail_soup = BeautifulSoup(detail_resp.text, "html.parser")
                    tables = detail_soup.select("table.bbs-table-view")

                    question_text = tables[0].find_all("tr")[-1].get_text(separator="\n", strip=True) if len(tables) > 0 else ""
                    answer_text = tables[1].find_all("tr")[-1].get_text(separator="\n", strip=True) if len(tables) > 1 else ""

                    #  질문/답변만 사용, 공백 또는 형식 오류 데이터 제거
                    if question_text.strip() and answer_text.strip():
                        data_item = {
                            "instruction": question_text.strip(),  # 민원 내용만!
                            "output": answer_text.strip()          # 실제 답변만!
                        }
                        tinyllama_data.append(data_item)
                        print("✅ 민원 수집:", title)

# ✅ JSONL 파일로 저장 (각 줄마다 하나의 JSON 객체)
with open("data.jsonl", "w", encoding="utf-8") as f:
    for item in tinyllama_data:
        json_line = json.dumps(item, ensure_ascii=False)
        f.write(json_line + "\n")

print(f"🎉 총 {len(tinyllama_data)}개의 데이터가 tinyllama_data.jsonl에 저장되었습니다.")