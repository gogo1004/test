inputs = [
    ['가', '나', '다', '라', '마', '', '바', '사', '아', '', '자'],
    ['aa', 'ttt', '2', '3', '3', '', '2', '3', '4', '', '1'],
    ['', 'ddd', '2', '3', '3', '', '2', '3', '4', '', '1'],
    ['bb', 'fff', '2', '3', '7', '', '2', '3', '8', '', '1'],
    ['', 'hhh', '2', '3', '7', '', '2', '3', '8', '', '1']
]

# 공백을 삭제하고 나누는 함수
def process_row(row):
    groups = [[]]
    for item in row:
        if item != '':
            groups[-1].append(item)
        else:
            groups.append([])
    return groups

# 실제 처리 과정
new_matrix = []
for row in inputs:
    processed_row = process_row(row)
    new_row = [' '.join(group) if group else 'null' for group in processed_row]
    new_matrix.append(new_row)

# 결과 출력
for row in new_matrix:
    print('\t'.join(row))
