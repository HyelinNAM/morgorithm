bodies = [list(map(int,input().split())) for _ in range(int(input()))]

for idx, b in enumerate(bodies):

    rank = 1

    for idx2, c in enumerate(bodies):
        if idx == idx2:
            pass

        if (b[0] < c[0]) and (b[1] < c[1]):
            rank += 1

    print(rank, end=' ')
