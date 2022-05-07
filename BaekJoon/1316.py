# 그룹 단어 체커

words = [input() for _ in range(int(input()))]
answer = 0

for word in words:

    group = True
    alphabet = {}

    for idx in range(len(word)-1):

        if alphabet.get(word[idx]):
            group = False
            break

        if word[idx] != word[idx+1]:
            alphabet[word[idx]] = True

    # 마지막 글자 따로 검사
    if alphabet.get(word[-1]):
        group = False

    if group:
        answer += 1

print(answer)