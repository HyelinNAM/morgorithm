# 요세푸스 문제
from collections import deque

n, k = map(int, input().split())
dq = deque([str(i+1) for i in range(n)])

answer = []
count = 1


while dq:
    if count % k == 0:
        answer.append(dq.popleft())

    else:
        tmp = dq.popleft()
        dq.append(tmp)

    count +=1 

print(f"<{', '.join(answer)}>")