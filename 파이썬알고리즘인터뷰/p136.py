# 주어진 문자열이 팰린드롬(회문)인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# 1.
def isPalindrome(sentence:str) -> bool:
    strs = []

    for char in sentence:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# 2. Deque
from collections import deque

def isPalindrome(sentence:str) -> bool:
    strs:deque = deque()

    for char in sentence:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 3. 슬라이싱
import re

def isPalindrome(sentence:str) -> bool:

    sentence = sentence.lower()
    sentence = re.sub('[^a-z0-9]','',sentence) # string

    return sentence == sentence[::-1]


sentence = input('회문 입력:')
print(isPalindrome(sentence))
