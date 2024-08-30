import streamlit as st
from datetime import datetime

# 애플리케이션 제목
st.title("학생 결석 사유 입력")

# 학생 학번 입력
student_id = st.text_input("학생 학번을 입력하세요:")

# 학생 이름 입력
student_name = st.text_input("학생 이름을 입력하세요:")

# 결석 종류 선택
absence_type = st.selectbox(
    "결석 종류를 선택하세요:",
    ["질병결석", "인정결석", "기타결석"]
)

# 결석 날짜 선택
absence_date = st.date_input(
    "결석 날짜를 선택하세요:",
    value=datetime.today()
)

# 결석 사유 입력
reason = st.text_area("결석 사유를 서술하세요:")

# 제출 버튼
if st.button("제출"):
    if not student_id.strip() or not student_name.strip():
        st.error("학번과 이름을 모두 입력해 주세요.")
    elif not reason.strip():
        st.error("결석 사유를 입력해 주세요.")
    else:
        # 제출된 정보 출력
        st.success("결석 사유가 성공적으로 제출되었습니다.")
        st.write("### 입력된 정보")
        st.write(f"- **학번**: {student_id}")
        st.write(f"- **이름**: {student_name}")
        st.write(f"- **결석 종류**: {absence_type}")
        st.write(f"- **결석 날짜**: {absence_date.strftime('%Y-%m-%d')}")
        st.write(f"- **사유**: {reason}")

# 기존 제출된 정보 보기 (기능 확장을 위한 섹션)
st.sidebar.title("기존 제출된 정보 보기")
st.sidebar.info("현재 저장된 데이터는 없음. 나중에 데이터베이스 기능을 추가할 수 있습니다.")
