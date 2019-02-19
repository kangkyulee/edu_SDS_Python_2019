import re
import pandas as pd

# 실습데이터 만들기
text1 = "1234 asdfASDF  ㄱㄴㄷㄹㅏㅑㅓㅕ가나다라   .!@#"
text2 = "<a> <ab> <abc> <abcd>"
text3 = pd.Series(["aaa", "bbb", "ccc", "abc"])

# text1
# 숫자 치환

# 영문 치환
# __ 소문자 치환

# __ 대문자 치환

# 한글 치환
# __ 자음 치환

# __ 모음 치환

# __ 완성형 치환

# 띄어쓰기 치환


# 응용
# __ 숫자가 아닌 모든 문자 치환

# __ 영문자가 아닌 모든 문자 치환

# __ 한글이 아닌 모든 문자 치환

# __ 숫자와 영문 대문자가 아닌 모든 문자 치환

# __ 숫자 2, 3만 치환

# __ 숫자 2, 3, 4, 7, 8, 9 치환

# __ '.'의 치환

# __ 두 칸 띄어쓰기와 세 칸 띄어쓰기의 치환

# __ "asdf"와 "가나다라" 치환


# 특수문자내 문자 처리(text2)
# __ 모든 경우의 수 치환

# __ 내부 문자 1개 치환

# __ 내부 문자 2~4개 치환

# 텍스트 조건(text3)
# __ "a"를 포함하는 원소 추출

# __ "b"를 포함하는 원소 추출

# __ "b"로 시작하는 원소 추출

# __ "a"로 끝나는 원소 추출

# __ "a"또는 "b"를 포함하는 원소 추출
