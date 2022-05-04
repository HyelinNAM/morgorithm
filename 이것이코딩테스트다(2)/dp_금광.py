import numpy as np

T = int(input()) # 테스트 케이스 개수

for t in range(T):

    n, m = map(int, input().split()) # n x m
    golds = list(map(int, input().split()))
    golds = (np.array(golds).reshape(n,m)).tolist()

    for j in range(1,m):
        for i in range(n):

            lu, ll, ld = -1, -1, -1

            # 왼쪽 위
            if i-1 >= 0 and j-1 >= 0:
                lu = golds[i][j] + golds[i-1][j-1]

            # 왼쪽
            if j-1 >= 0:
                ll = golds[i][j] + golds[i][j-1]

            # 왼쪽 아래
            if i+1 < n and j-1 >= 0:
                ld = golds[i][j] + golds[i+1][j-1]

            golds[i][j] = max(lu, ll, ld)

    print(max(np.array(golds).T[-1]))