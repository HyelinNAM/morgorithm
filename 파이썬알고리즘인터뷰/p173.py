# 두 수의 합 (덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스 리턴)

def two_sum(nums, target):

    nums_map = {}

    # 숫자를 key로 인덱스를 value로 dict 저장
    for i, num in enumerate(nums):
        nums_map[num] = i # 2:0, 7:1, 11:2, 15:3

    for i, num in enumerate(nums):
        if (target-num) in nums_map and i != nums_map[target-num]: # 자기자신 예외처리
            return nums.index(num), nums_map[target-num]

nums = [2,7,11,15]
target = 18
two_sum(nums, target)
