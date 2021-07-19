# 어렵다!

# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산

# 투 포인터
# 최대 높이를 기점으로 왼쪽/오른쪽에서 접근
def cal_water(heights):

    if not heights:
        return 0
    
    water = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]

    while left < right:
        left_max, right_max = max(heights[left], left_max), max(heights[right], right_max)

        if left_max <= right_max:
            water += left_max - heights[left]
            left += 1
        
        else:
            water += right_max - heights[right]
            right -= 1

    return water

# 스택
def cal_water(heights):
    stack = []
    water = 0

    for i in range(len(heights)):

        while stack and heights[i] > heights[stack[-1]]:

            top = stack.pop()

            if not len(stack): # len(stack)이 0이면
                break

            distance = i - stack[-1] -1
            waters = min(heights[i], heights[stack[-1]]) - heights[top]

            water += distance * waters
        
        stack.append(i)

    return water
            
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
cal_water(heights)