n = int(input())
numbers = list(map(int, input().split()))

dp = [1] * n

for j in range(1, n): # 수열 끝나는 포인트
    for i in range(0,j): # 0 ~ i-1 # 수열 시작하는 포인트
        if numbers[i] < numbers[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))