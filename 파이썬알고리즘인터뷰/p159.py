# 가장 긴 팰린드롬 부분 문자열

import re

# 혜린
def longest_palindrom(input):

    # 예외처리 추가
    if len(input) < 2 or input == input[::-1]:
        return input

    def is_palindrome(sentence:str) -> bool:

        sentence = sentence.lower()
        sentence = re.sub('[^a-z0-9]','',sentence) # string

        return sentence == sentence[::-1]

    pal = []

    length = len(input) - 1 #len(input) -> 예외처리에서 이미.

    while not pal:

        l, r = 0, length

        while r <= len(input):
            if is_palindrome(input[l:r]):
                pal.append(input[l:r])
            
            l += 1
            r  = l + length

        length -= 1

    return pal

input = "abcba"
longest_palindrom(input)