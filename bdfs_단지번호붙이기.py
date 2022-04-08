n = int(input())

graph = []
result = []

for i in range(n):
    graph.append([int(s) for s in input()])

def dfs(x,y, count):

    if x <0 or x>=n or y <0 or y>=n:
        return count

    if graph[x][y] == 1:
        
        graph[x][y] = 0 # 방문처리

        count = dfs(x-1,y,count)
        count = dfs(x+1,y,count)
        count = dfs(x,y-1,count)
        count = dfs(x,y+1,count)

        return count+1

    return count

for i in range(n):
    for j in range(n):
        
        count = 0
        tmp = dfs(i,j,count)

        if tmp != 0:
            result.append(tmp)

result.sort()
print(len(result))
print(*result, sep='\n')