from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append([int(s) for s in input()])

distance = [[0 for i in range(m)] for j in range(n)]


def bfs(graph,distance):

    queue = deque([(0,0)])

    distance[0][0] += 1
    graph[0][0] = 0

    while queue:

        v = queue.popleft()

        # 상하좌우
        for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:

            if v[0] + x < 0 or v[0] + x >= n or v[1] + y < 0 or v[1] + y >= m:
                continue

            if graph[v[0]+x][v[1]+y] == 1:
                queue.append((v[0]+x, v[1]+y))
                distance[v[0]+x][v[1]+y] = distance[v[0]][v[1]] + 1
                graph[v[0]+x][v[1]+y] = 0

bfs(graph, distance)

print(distance[n-1][m-1])


# 이코테 예시 코드
# 흐름은 같았으나, 코드가 좀 더 간결했음

# from collections import deque

# n, m = map(int, input().split())

# graph = []

# for i in range(n):
# 	graph.append(list(map(int,input())))
    
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
	
#     queue = deque()
#     queue.append((x,y))
    
#     while queue:
#     	x, y = queue.popleft()
        
#         for i in range(4):
#         	nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx<0 or nx >=n or ny<0 or ny>= m:
#             	continue
                
#             if graph[nx][ny] = 0:
#             	continue
                
#             if graph[nx][ny] == 1:
#             	graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx,ny))
                
# 	return graph[n-1][m-1]