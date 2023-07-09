def count_words(text):
    # 입력된 텍스트를 공백을 기준으로 분할하여 단어의 개수를 계산합니다.
    words = text.split()
    word_count = len(words)
    return word_count

# 사용자로부터 텍스트를 입력받습니다.
text = input("텍스트를 입력하세요: ")

# 단어 개수를 출력합니다.
print("텍스트 내 단어 개수:", count_words(text))