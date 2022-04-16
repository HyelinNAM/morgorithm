N = int(input())
scores = list(map(int,input().split()))

scores = [s/max(scores) * 100 for s in scores]

print(sum(scores)/N)