string = input()
nums = [int(s) for s in string]

result = nums[0]

for num in nums[1:]:
    #if num == 0 or num == 1 or result == 0 or result == 1:
    if num <= 1 or result <=1:
        result += num

    else:
        result = result * num

print(result)
