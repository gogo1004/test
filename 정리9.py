with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip().split("\t") for line in file]

    # input.txt 파일을 열고, 줄 단위로 읽어서 lines 리스트에 저장합니다.
    # 각 줄은 탭으로 구분된 문자열로 저장됩니다.

for i, line in enumerate(lines):
    if line[0]:
        column_count = len(line) + len(lines[i + 1]) + 1
        break

    # lines 리스트에서 첫 번째 줄을 찾습니다.
    # 첫 번째 줄이 비어 있지 않으면, 해당 줄의 길이 + 다음 줄의 길이 + 1을 column_count 변수에 저장합니다.

processed_lines = [[""] * column_count]
i = 0

    # column_count 개의 공백 문자열로 이루어진 리스트를 생성합니다.
    # i 변수를 0으로 초기화합니다.

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

    # i 값이 lines 리스트의 길이보다 작을 때까지 반복합니다.
    # 각 반복마다 lines 리스트의 i 번째 줄을 가져옵니다.
    # i 번째 줄이 비어 있지 않으면, 해당 줄 + 다음 줄 + 다음 다음 줄의 첫 번째 문자를 processed_line 리스트에 추가합니다.
    # 데이터 줄의 길이가 column_count보다 작은 경우 "##" 문자를 추가합니다.
    # processed_lines 리스트에 processed_line 리스트를 추가합니다.
    # i 값을 3 증가시킵니다.

with open("output.txt", "w", encoding="utf-8") as output_file:
    for line in processed_lines:
        output_file.write("\t".join(line) + "\n")

print("새롭게 정렬된 출력이 output.txt 파일에 저장되었습니다.")

    # processed_lines 리스트를 순회하면서, 각 줄을 output.txt 파일에 탭으로 구분하여 출력합니다.
    # 출력 후 "새롭게 정렬된 출력이 output.txt 파일에 저장되었습니다."를 출력합니다.

