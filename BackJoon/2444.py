# 별 찍기 - 6

n = int(input())

for i,j in enumerate(range(1,2*n-1,2)):
    print((' ' * (n-i-1)) +('*' * j))

for i,j in enumerate(range(2*n-1,0,-2)):
    print((' ' * i) +('*' * j))