# 뼈대문제 - 큐
import sys
from collections import deque

input=sys.stdin.readline
n = int(input())
dq = deque()

for _ in range(n):
    order = input().split()

    if order[0] == 'push_front':
        dq.appendleft(order[1])

    elif order[0] == 'push_back':
        dq.append(order[1])

    elif order[0] == 'pop_front':
        print(dq.popleft() if dq else -1)

    elif order[0] == 'pop_back':
        print(dq.pop() if dq else -1)

    elif order[0] == 'size':
        print(len(dq))

    elif order[0] == 'empty':
        print(0 if dq else 1)

    elif order[0] == 'front':
        print(dq[0] if dq else -1)
    
    else: # back
        print(dq[-1] if dq else -1)
        