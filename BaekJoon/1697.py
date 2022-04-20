# 숨바꼭질
from collections import deque

N, K = map(int, input().split()) # 수빈 >> 동생

queue = deque([N])
visited = {N:True}
pop_count = 1
answer = 0

if N>=K:
    answer = N-K

else:
    while queue:
        tmp = 0
        answer += 1

        for _ in range(pop_count):
            top = queue.popleft()

            candidates = [top*2, top+1, top-1]

            if K in candidates:
                queue.clear()
                break

            for c in candidates:
                if c>= 0 and c <= 100000 and not visited.get(c):
                    visited[c] = True
                    queue.append(c)
                    tmp += 1
        
        pop_count = tmp

print(answer)