n = int(input())
numbers = list(map(int, input().split()))

unique_numbers = sorted(list(set(numbers)))
num_dict = {num:i for i, num in enumerate(unique_numbers)}

for n in numbers:
    print(num_dict[n], end=' ')