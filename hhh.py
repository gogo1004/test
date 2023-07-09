# data = '''\
# NODE   OPER                aaaaaaa     ddddddd    tttttttt   kkkkkkkkk      rereee    gggggggg  llllllllll     eeeeeee     cccccc   nnnnnnnnn  RES_TIME     C_RATIO   HIT_RATIO
# DBC3   ADD                    6605        6605           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        DEL                    6550        6550           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        SET                  563317      563318           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        CHKOUT               570326      563580      563697        6629           0           0         116           0           0           0 0.00       98.82       98.84
#        SETSID                  571         569         569           2           0           0           0           0           0           0 0.00       99.65       99.65
# DBC4   ADD                    6670        6670           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        DEL                    6700        6700           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        SET                  560624      560625           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        CHKOUT               567788      560973      561110        6678           0           0         137           0           0           0 0.00       98.80       98.82
#        SETSID                  581         581         581           0           0           0           0           0           0           0 0.00      100.00      100.00
# DBC5   ADD                    6410        6410           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        DEL                    6284        6284           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        SET                  558536      558536           0           0           0           0           0           0           0           0 0.00      100.00        0.00
#        CHKOUT               565246      558703      558817        6429           0           0         114           0           0           0 0.00       98.84       98.86
#        SETSID                  548         548         548           0           0           0           0           0           0           0 0.00      100.00      100.00
# '''

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

