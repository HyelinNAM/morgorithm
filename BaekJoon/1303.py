# 전쟁 - 전투

n, m = map(int, input().split()) # n - 가로(열), m - 세로(행)
wars = [list(input()) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * n for _ in range(m)]

def dfs(team, x, y, visited, count):

    if x < 0 or x >= m:
        return count

    if y < 0 or y >= n:
        return count

    if wars[x][y] == team:
        if not visited[x][y]:
            visited[x][y] = True

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                count = dfs(team, nx, ny, visited, count)
    
            # count = dfs(team, x+1, y, visited, count)
            # count = dfs(team, x, y+1, visited, count)
            # count = dfs(team, x-1, y, visited, count)
            # count = dfs(team, x, y-1, visited, count)

            return count + 1
    
    return count

white, blue = 0, 0

for i in range(m):
    for j in range(n):
        if wars[i][j] == 'W' and not visited[i][j]:
            white += (dfs('W',i,j, visited, 0) ** 2)
        if wars[i][j] == 'B' and not visited[i][j]:
            blue += (dfs('B',i, j, visited, 0) ** 2) 
        
print(white, blue)