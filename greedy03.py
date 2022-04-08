n = int(input())
fears = list(map(int, input().split()))
fears.sort()

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for f in fears:
    
    count +=1 

    if count >= f:
        result += 1
        count = 0

print(result)

