# 한글 주석
# 이 코드는 input.txt 파일의 내용을 읽어와서
# output.txt 파일에 정렬된 출력으로 저장한다.

with open("input.txt", "r", encoding="utf-8") as file:
    # lines 변수에 input.txt 파일의 내용을 저장한다.
    # 각 줄은 공백으로 구분된 단어들의 목록으로 저장된다.
    lines = [line.strip().split() for line in file]

    # 임시 출력
    # 각 줄의 내용을 공백으로 구분하여 출력한다.
    # for line in lines:
    #     print(" ".join(line))

    # column_count 변수에 각 줄의 최대 길이를 저장한다.
    # 예를 들어, input.txt 파일의 첫 번째 줄이 "이름 나이"이고,
    # 두 번째 줄이 "홍길동 30"이면 column_count는 5가 된다.
    for i, line in enumerate(lines):
        print (i, len(line))
        if i == 0:
            continue
        head_line_0 = len(line)
        if head_line_0 == len(line):
            반복주기 = i
            print (반복주기)
            break
        
    for i, line in enumerate(lines):
        print ("i, line =" ,i, line)
        if line[0]:
            column_count = len(line) + len(lines[i + 1]) # 제목 줄를 참조하여 출력 할 컬럼 갯수를 구함
            break

    # processed_lines 변수에 정렬된 출력을 저장한다.
    # 각 줄은 column_count개의 요소를 가진다.
    # 요소가 없는 경우 "##"로 채워진다.
    processed_lines = [[""] * column_count]

    i = 0
    
    # 각 줄을 순회하면서 processed_lines 변수에 저장한다.
    while i < len(lines):
        line = lines[i]
        print (line, lines[i + 1])
        if line[0]:
            # line과 lines[i + 1]을 합쳐서 processed_lines에 저장한다.
            processed_line = line + lines[i + 1]
            # 데이터 줄의 길이가 column_count보다 작은 경우 "##" 추가
            while len(processed_line) < column_count:
                processed_line.insert(0, "##")
            # processed_lines에 processed_line을 추가한다.
            processed_lines.append(processed_line)
            i += 2  # 반복 라인 수 설정
        else:
            # line[1:]은 line의 두 번째 요소부터 끝까지의 요소들을 가리킨다.
            # processed_line은 ["##"] + line[1:] + lines[i + 1]로 구성된다.
            processed_line = ["##"] + line[1:] + lines[i + 1]

            # 데이터 줄의 길이가 column_count보다 작은 경우 "##" 추가
            while len(processed_line) < column_count:
                processed_line.insert(0, "##")

            # processed_lines의 마지막 요소를 processed_line으로 교체한다.
            processed_lines[-1] = processed_line
            i += 2

    # processed_lines의 내용을 output.txt 파일에 저장한다.
    with open("output.txt", "w", encoding="utf-8") as output_file:
        for line in processed_lines:
            output_file.write(" ".join(line) + "\n")

    print("새롭게 정렬된 출력이 output.txt 파일에 저장되었습니다.")
