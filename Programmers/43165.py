# 타겟 넘버

# bfs

from collections import deque

def solution(numbers, target):

    queue = deque([numbers[0], -numbers[0]])
    count = 2
    
    for n in numbers[1:]:
        for _ in range(count):
            top = queue.popleft()
            queue.append(top+n)
            queue.append(top-n)
        
        count *= 2

    return queue.count(target)

# dfs

