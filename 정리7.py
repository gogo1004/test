with open("input_test.txt", "r", encoding="utf-8") as file:
    lines = [line.strip().split("\t") for line in file]

# 첫 작업 블록 찾기
for i, line in enumerate(lines):
    if line[0]:
        # 첫 번째 줄의 항목 개수 구하기
        column_count = len(line) + len(lines[i + 1]) + 1
        break

# 최종 정리된 데이터를 저장할 빈 리스트 생성
processed_lines = [[""] * column_count]
i = 0

while i < len(lines):
    line = lines[i]

    if line[0]:
        processed_lines.append(line + lines[i + 1] + [lines[i + 2][0]])
        i += 3
    else:
        processed_lines[-1] = ["##"] + line[1:] + lines[i + 1] + [lines[i + 2][0]]
        i += 3

with open("output.txt", "w", encoding="utf-8") as output_file:
    for line in processed_lines:
        output_file.write("\t".join(line) + "\n")

print("정렬된 출력이 output.txt 파일에 저장되었습니다.")
