from collections import deque

n = int(input())

dp = [0] * n # 숫자를 바로 인덱스로 사용

queue = deque([(n,1)])

while queue:
    
    i,c = queue.popleft()

    if i % 5 == 0 and dp[i//5] == 0:
        dp[i//5] = c
        queue.append((i//5,c+1))

    elif i % 3 == 0 and dp[i//3] == 0:
        dp[i//3] = c
        queue.append((i//3,c+1))

    elif i % 2 == 0 and dp[i//2] == 0:
        dp[i//2] = c
        queue.append((i//2,c+1))

    if dp[i-1] == 0:
        dp[i-1] = c
        queue.append((i-1,c+1))

    if dp[1] != 0:
        break

print(dp[1])
