from bisect import bisect_left, bisect_right

n, x = map(int, input().split()) # n - 입력될 정수 개수, x - 찾아야하는 정수
numbers = list(map(int, input().split()))

""" 
count > 시간복잡도 O(N)
answer = numbers.count(x) if numbers.count(x) != 0 else -1
 
"""
left = bisect_left(numbers, x)
right = bisect_right(numbers, x)

print(left, right)

answer = right - left if right-left != 0 else -1

print(answer)