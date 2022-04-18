# 네트워크

def solution(n, computers):
    
    network = 0
    visited = [False] * len(computers[0])
    
    for v in visited:
        if not v:
            network += dfs(computers,v,visited,network)

    return network

def dfs(graphs, v, visited, network):
    visited[v] = True
    
    for i,j in enumerate(graphs[v]):
        if j == 1:
            if not visited[i]:
                dfs(graphs, i, visited, network)
    
    network += 1

    return network

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))