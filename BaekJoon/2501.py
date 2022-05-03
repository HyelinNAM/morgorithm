N, K = map(int, input().split())

# 약수 계산
divisors = [i for i in range(1,N+1)  if N%i == 0]

if len(divisors) >= K:
    print(divisors[K-1])

else:
    print(0)