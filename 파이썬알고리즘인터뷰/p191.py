# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력
# + 입력값은 항상 2n개가 되겠다!

def array_partition(nums):

    nums.sort()
    pair = []
    sum = 0

    for i, num in enumerate(nums):
        pair.append(num)

        if i % 2 !=0: # 홀수 = 짝수번째 순서
            sum += min(pair)
            pair = []

    return sum

# 정렬된 상태에서 min은 항상 짝수번째에 위치
def array_partition(nums):

    nums.sort()
    sum = 0

    for i, num in enumerate(nums):
        if i % 2 ==0: # 홀수 = 짝수번째 순서
            sum += num

    return sum

# Pythonic
def array_partition(nums):
    return sum(sorted(nums)[::2])


nums = [1,4,3,2]
array_partition(nums)