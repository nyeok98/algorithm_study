from collections import deque

graph = []
queue = deque()

m, n = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
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

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

bfs()
isZero = False
maxi = 0
for i in graph:
    for j in i:
        if j == 0:
            isZero = True
            continue
        maxi = max(maxi, j)

maxi -= 1
if isZero:
    maxi = -1

print(maxi)