# 2021 카카오 블라인드 리쿠르팅 - 신규 아이디 추천 

import re

def solution(new_id):
    # step 1
    answer = new_id.lower()
    # step 2
    answer = re.sub('[^a-z\d\-\_\.]', '', answer)
    # step 3
    while '..' in answer:
        answer = answer.replace('..','.')
    # step 4
    answer = answer.strip('.')
    # step 5
    answer = 'a' if len(answer) == 0 else answer
    # step 6
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    # step 7
    answer = answer + answer[-1] * (3-len(answer))if len(answer) <= 2 else answer

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))