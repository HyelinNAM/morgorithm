numbers = [int(input()) for _ in range(9)]

biggest = max(numbers)
idx = numbers.index(biggest)

print(biggest)
print(idx+1)