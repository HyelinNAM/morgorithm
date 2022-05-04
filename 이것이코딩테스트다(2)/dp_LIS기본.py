# n = int(input())
# array = list(map(int, input().split()))

n = 7
array = [4,2,5,8,4,11,15]

dp = [1] * n

for i in range(1, n):
	for j in range(0, i):
		if array[j] < array[i]:
			dp[i] = max(dp[i], dp[j] + 1)

print(dp)