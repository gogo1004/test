import sys

def main():
    # 파일 입력
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    # 정렬
    data.sort(key=lambda x: x[0])

    # 출력
    for row in data:
        print("".join(row))

if __name__ == "__main__":
    main()