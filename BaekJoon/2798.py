from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

combi = list(combinations(cards, 3))

tmp = sorted([sum(c) for c in combi if sum(c) <= m], reverse=True)

print(tmp[0])