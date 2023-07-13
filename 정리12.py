# 데이터를 저장할 리스트 생성
data = []

# 텍스트 파일 열기
with open('input.txt', 'r', encoding="utf-8") as file:
    # 첫 번째 라인 읽기
    first_line = file.readline().strip()
    print (first_line)
    # 첫 번째 라인의 컬럼 개수 계산 및 저장
    column_counter = len(first_line.split(' '))
    print (column_counter)

    # 데이터 리스트에 첫 번째 라인 추가
    data.append(first_line)

    # 다음 라인부터 반복해서 처리
    for line in file:
        line = line.strip()
        if len(line.split(' ')) < column_counter:
            # 컬럼 개수가 작은 경우 첫 번째 라인과 합치기
            data[-1] += line
        else:
            # 컬럼 개수가 같거나 큰 경우 데이터 리스트에 추가
            data.append(line)

# 결과 출력
for line in data:
    print(line)
