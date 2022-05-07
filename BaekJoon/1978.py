N = int(input())
numbers = list(map(int, input().split()))

answer = 0 

for n in numbers:

    if n == 1:
        answer += 1
        continue

    else:
        for i in range(2, n):
            if n % i == 0:
                answer += 1
                break

print(N-answer)