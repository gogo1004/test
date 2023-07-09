
# 파이썬 모듈 `sys`와 `io`를 가져옵니다.
import sys
import io

# `zzz.txt` 파일을 읽어 `data` 변수에 저장합니다.
with io.open("SMF.txt", "r", encoding="utf-8") as f:
  data = f.read().splitlines()

# `result` 변수를 생성합니다.
result = []

# `data` 변수의 각 행을 `row` 변수에 저장하고, `row` 변수의 각 단어를 공백으로 구분하여 `result` 변수에 추가합니다.
for row in data:
    result.append(" ".join(row.split()))

# `max_col` 변수를 사용하여 각 열의 최대 길이를 계산합니다.
max_col = max(len(row.split()) for row in data)

# `result` 변수의 각 행을 반복하면서, 행의 길이가 `max_col`과 같아질 때까지 공백 문자를 추가합니다.
for row in result:
  while len(row) < max_col:
    row.append("")

# `result` 변수의 각 행을 줄 바꿈으로 구분하여 출력합니다.
print("\n".join(result))
