# 별 찍기 - 5

n = int(input())

for i, j in enumerate(range(1,2*n+1,2)):
    print((' '*(n-i-1)) + ('*' * j))