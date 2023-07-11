# input.txt 파일 열기 및 읽기, utf-8로 인코딩
with open("input.txt", "r", encoding="utf-8") as file:
    # 파일의 각 줄을 탭으로 분할하여 리스트로 변환
    lines = [line.strip().split("\t") for line in file]
    print (lines)

# 최종 정리된 데이터를 저장할 빈 리스트 생성
processed_lines = [[""] * 9]
i = 0

# 입력된 줄을 순회하며 데이터 정리 작업 수행
while i < len(lines):
    line = lines[i]

    # 첫 번째 항목이 비어있지 않으면 블록의 시작 부분
    if line[0]:
        # 현재 줄, 다음 줄, 그 다음 줄의 첫 번째 항목을 하나의 줄에 합치기
        processed_lines.append(line + lines[i + 1] + [lines[i + 2][0]])
        i += 3
    else:
        # 기존의 마지막 라인을 새로운 라인으로 수정
        processed_lines[-1] = ["##"] + line[1:] + lines[i + 1] + [lines[i + 2][0]]
        i += 3

# output.txt 파일에 정리된 데이터 저장
with open("output.txt", "w", encoding="utf-8") as output_file:
    for line in processed_lines:
        output_file.write("\t".join(line) + "\n")

print("정렬된 출력이 output.txt 파일에 저장되었습니다.")
