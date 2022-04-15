n, m = map(int, input().split()) # n - 떡볶이 떡 / m - 요청한 떡의 길이
heights = list(map(int, input().split()))

start = 0
end = max(heights) # >>> idx 이기 때문에

def check_condition(array, target, h):
    tmp = [0 if a <= h else a-h for a in array]

    if sum(tmp) >= target:
        return True
    
    else:
        return False

result = 0

while start <= end:
    mid = (start+end) // 2

    if check_condition(heights, m, mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)