# 네트워크

from collections import deque

# bfs
def solution(n, computers):
    
    visited = [False] * n
    network = 0
    
    for no in range(n): # n - 노드 넘버
        if not visited[no]: # 아직 방문 X
            visited[no] = True
            queue = deque([no])
            
            while queue:
                v = queue.popleft()
                
                for i,j in enumerate(computers[v]):
                    if j == 1:
                        if not visited[i]:
                            queue.append(i)
                            visited[i] = True

            network += 1
            
        else:
            continue
    
    return network

# dfs
def solution(n, computers):
    
    visited = [False] * n
    network = 0
    
    def bfs(computers,no,visited):

        visited[no] = True
        
        for i, j in enumerate(computers[no]):
            if j == 1:
                if not visited[i]:
                    bfs(computers,i,visited)

    for no in range(n): # n - 노드 넘버
        if not visited[no]: # 아직 방문 X

            bfs(computers,no,visited)

            network += 1

        else:
            continue
    
    return network

print(solution(5,[[1,1,1,0,0,],[1,1,0,0,0],[1,0,1,0,0],[0,0,0,1,1],[0,0,0,1,1]]))