with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip().split() for line in file]

FirstColumnCount = len(lines[0])
print(FirstColumnCount)

with open("output.txt", "w", encoding="utf-8") as outfile:
    for i, line in enumerate(lines):
        if i == 0:
            outfile.write(" ".join(line))  # 첫 번째 줄 쓰기
        elif i != FirstColumnCount:
            # 첫 번째 줄을 제외하고는 RES_TIME, C_RATIO, HIT_RATIO의 정보를 같은 줄에 추가
            outfile.write(" " + " ".join(line) + "\n")
        # else:
        #     # 그 외 줄은 줄 바꿈 없이 이어서 작성
        #     outfile.write(" ".join(line) + " ")

# 결과 출력
with open("output.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())