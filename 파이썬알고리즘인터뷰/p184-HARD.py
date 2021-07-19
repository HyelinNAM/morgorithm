# 배열을 입력받아 합으로 0으로 만들 수 있는 3개의 엘리먼트 출력

# 혜린 - 투포인터

'''
1. 왼쪽 포인터를 오른쪽으로 옮겨가고, 오른쪽 포인터는 항상 맨 오른쪽에서 시작하는 방법 --> 불가능
2. 

'''

def three_sum(nums):

    results = []
    nums.sort()

    for i in range(len(nums)-2):
        left, right = i, len(nums) - 1

        if i>0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums) - 1 # 투포인터

        while left < right:

            sum = nums[i] + nums[left] + nums[right]

            if sum < 0:
                left += 1

            elif sum == 0: # 세트 찾았다고 끝 X. 남은 경우 더 탐색.
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

            else: # >0
                right -= 1

    return results

nums = [-1,0,1,2,-1,4]
three_sum(nums)