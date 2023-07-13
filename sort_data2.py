with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip().split() for line in file]

    print (lines)

header_line = lines[0] + lines[1] + lines[2]
data_lines = lines[3:]

output_lines = []
output_lines.append(" ".join(header_line))

for idx, data_line in enumerate(data_lines):
    if idx % 2 == 0:
        # 첫 번째 라인의 데이터를 그대로 가져오기
        output_lines.append(" ".join(data_line))
    else:
        # 데이터가 없는 부분에 "###" 추가
        output_lines.append(" ".join(["###", data_line[0]] + data_line[1:]))

with open("output.txt", "w", encoding="utf-8") as output_file:
    for line in output_lines:
        output_file.write(line + "\n")

print("정렬된 출력이 output.txt 파일에 저장되었습니다.")
