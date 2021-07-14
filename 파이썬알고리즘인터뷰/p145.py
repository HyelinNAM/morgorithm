# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

# 1. 투 포인터 스왑
# 혜린
def reverse_string(s):

    s = [char for char in s] # 문자열 -> 리스트 전처리

    print(f'array: {s}')

    fro = 0
    end = len(s) - 1

    while end > fro:

        tmp = s[end]
        s[end] = s[fro]
        s[fro] = tmp

        fro += 1
        end -= 1
    
    print(f'result: {s}')

# 책
def reverse_string(s):

    s = [char for char in s]

    print(f'array: {s}')

    left, right = 0, len(s) -1

    while left < right:

        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1
    
    print(f'result: {s}')

# 2. 문자열 슬라이싱
def reverse_string(s):

    s = [char for char in s]

    print(f'array: {s}')

    s = s[::-1] 
    # s[:] = s[::-1]
    # s.reverse()

    print(f'result: {s}')


s = input("문자열 리스트(배열): ")
reverse_string(s)
