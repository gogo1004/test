with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip().split() for line in file]

# 결과 출력
for line in lines:
    print(" ".join(line))
