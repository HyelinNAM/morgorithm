N, M = map(int, input().split())

money = [int(input()) for _ in range(N)]

d = [-1] * 10001 # 1 <= M <= 10,000
for m in money:
    d[m] = 1

for i in range(1,M+1):
    for m in money:
        if i-m >0 and d[i-m] != -1:
            if d[i] == -1:
                d[i] = d[i-m] + 1

            else:
                d[i] = min(d[i], d[i-m] +1)

print(d[M])