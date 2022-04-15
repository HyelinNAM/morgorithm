from collections import deque

numbers = list(map(int, input().split()))
target = int(input())

answer = 0
queue = deque()
n = len(numbers)

queue.append((numbers[0],0))
queue.append((-numbers[0],0))

while queue:
    temp, idx = queue.popleft()

    if idx < n:
        queue.append((temp + numbers[idx],idx+1))
        queue.append((temp - numbers[idx],idx+1))

    else:
        if temp == target:
            answer += 1

print(answer)