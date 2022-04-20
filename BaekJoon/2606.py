# 바이러스 ; 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 수?

# dfs
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
graphs = [list(map(int, input().split())) for _ in range(int(input()))]

new_graphs = [[0]*(n+1) for _ in range(n+1)] # 네트워크 표현용

for g in graphs:
    new_graphs[g[0]][g[1]] = 1
    new_graphs[g[1]][g[0]] = 1

visited = [False]  * (n+1) # 주어진 컴퓨터 번호를 바로 사용하기 위해 + 1

def dfs(v, graphs, visited):
    visited[v] = True

    for i,j in enumerate(new_graphs[v]):
        if j == 1:
            if not visited[i]:
                dfs(i, graphs, visited)

# new_graphs이용해서 1번과 연결된 컴퓨터 개수 세기만 하면 됨 (모든 노드 X)
dfs(1, graphs, visited)
print(sum(visited)-1)
