with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip().split("\t") for line in file]

for i, line in enumerate(lines):
    if line[0]:
        column_count = len(line) + len(lines[i + 1]) + 1
        break

processed_lines = [[""] * column_count]
i = 0

while i < len(lines):
    line = lines[i]

    if line[0]:
        processed_line = line + lines[i + 1] + [lines[i + 2][0]]
        # 데이터 줄의 길이가 column_count보다 작은 경우 "##" 추가
        while len(processed_line) < column_count:
            processed_line.insert(0, "##")  # 2번째 위치에 "##" 추가
        processed_lines.append(processed_line)
        i += 3
    else:
        processed_line = ["##"] + line[1:] + lines[i + 1] + [lines[i + 2][0]]
        # 데이터 줄의 길이가 column_count보다 작은 경우 "##" 추가
        while len(processed_line) < column_count:
            processed_line.insert(0, "##")  # 2번째 위치에 "##" 추가
        processed_lines[-1] = processed_line
        i += 3

with open("output.txt", "w", encoding="utf-8") as output_file:
    for line in processed_lines:
        output_file.write("\t".join(line) + "\n")

print("새롭게 정렬된 출력이 output.txt 파일에 저장되었습니다.")
