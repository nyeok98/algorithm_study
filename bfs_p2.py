from collections import deque

m, n = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if visited[x][y]:
        return
    global maxi
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0 or graph[nx][ny] > (graph[x][y] + 1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

isZero = False
maxi = 0
for i in range(n):
    for j in range(m):
        maxi = max(maxi, graph[i][j])
        if graph[i][j] == 0:
            isZero = True

maxi -= 1
if isZero:
    maxi = -1

print(maxi)