
import sys
import io

with io.open("SMF.txt", "r", encoding="utf-8") as f:
  data = f.read().splitlines()


data = '\n'.join(data)  # 리스트를 개행 문자로 연결하여 하나의 문자열로 변환
print (data)
# 주어진 데이터를 줄 단위로 분할합니다.
lines = data.split('\n')

# 포맷팅된 데이터를 저장할 리스트를 생성합니다.
formatted_data = []

# 각 열의 최대 너비를 찾기 위한 리스트를 생성합니다.
# 열의 수는 첫 번째 줄을 기준으로 결정됩니다.
column_widths = [0] * len(lines[0].split())

# 각 줄에 대해서 처리를 수행합니다.
for line in lines:
    # 빈 줄인 경우 건너뜁니다.
    if line.strip() == '':
        continue

    # 줄을 공백으로 분할합니다.
    line_parts = line.split()

    # 'NODE'로 시작하는 줄인 경우에는 원본 그대로 저장하고,
    # 최대 너비를 업데이트합니다.
    if line.startswith('NODE'):
        formatted_data.append(line)
        column_widths = [max(column_widths[i], len(line_parts[i])) for i in range(len(line_parts))]
    else:
        # 열의 수가 부족한 경우 'null' 값을 삽입합니다.
        if len(line_parts) < len(column_widths):
            line_parts = ['null'] * (len(column_widths) - len(line_parts)) + line_parts

        # 각 열을 최대 너비에 맞추어 왼쪽 정렬하고,
        # 너비에 2를 더해 공백을 추가합니다.
        formatted_line = ''.join(line_parts[i].ljust(column_widths[i] + 2) for i in range(len(column_widths)))

        # 포맷팅된 줄을 저장합니다.
        formatted_data.append(formatted_line)

# 리스트를 개행 문자로 연결하여 하나의 문자열로 만듭니다.
formatted_data = '\n'.join(formatted_data)

# 포맷팅된 데이터를 출력합니다.
print(formatted_data)

