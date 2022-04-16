numbers = [int(input()) for _ in range(7)]

# 홀수
odds = [n for n in numbers if n%2==1]

if odds:
    print(sum(odds))
    print(min(odds))

else:
    print(-1)