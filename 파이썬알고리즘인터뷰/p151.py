# 금지된 단어를 제외하고 가장 흔하게 등장하는 단어 출력하기 (대소문자 구분 X, 구두점도 무시)

import re
from collections import Counter

paragraph = "Bob hit a ball, the hit Ball flew far after it was hit."
banned = ["hit"]

def most_common(paragraph, banned):

    # 전처리
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]

    # Counts
    counts = Counter(words)

    return counts.most_common()[0][0]


most_common(paragraph, banned)
