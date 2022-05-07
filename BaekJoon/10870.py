import sys
sys.setrecursionlimit(10**6)

n = int(input())

# def fibo(i):

#     if i == 1 or i == 2:
#         return 1

#     else:
#         return fibo(i-1) + fibo(i-2)

# print(fibo(n))

# DP
dp = [0, 1]

for _ in range(n-1):
    dp = [dp[1], dp[0]+dp[1]]

print(dp[0] if n ==0 else dp[1])


