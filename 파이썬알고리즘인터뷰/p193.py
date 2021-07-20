
def array_product(nums):

    result = []
    p = 1

    for i in range(len(nums)):
        result.append(p)
        p = p * nums[i]

    p = 1
    for i in range(len(nums)-1, -1, -1): # 3,2,1,0
        result[i] = p * result[i]

        p = p * nums[i]

    return result

nums = [1,2,3,4]
array_product(nums)