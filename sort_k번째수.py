# array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬, k번째에 있는 수 구하기

array = [1, 5, 2, 6, 3, 7, 4] # list(map(int, input()))
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []

for start, end, idx in commands:
    arr = sorted(array[start-1:end])
    answer.append(arr[idx-1])

print(answer)