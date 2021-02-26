from collections import deque

queue = deque()

m, n, h = map(int, input().split())
graph = []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    graph.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if graph[nz][nx][ny] == -1:
                continue
            if graph[nz][nx][ny] == 0 or graph[nz][nx][ny] > (graph[z][x][y] + 1):
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

for z in range(h):
    for i in range(n):
        for j in range(m):
            if graph[z][i][j] == 1:
                queue.append((z, i, j))

bfs()
isZero = False
maxi = 0

for z in range(h):
    for i in range(n):
        for j in range(m):
            if graph[z][i][j] == 0:
                isZero = True
                continue
            maxi = max(maxi, graph[z][i][j])

maxi -= 1
if isZero:
    maxi = -1

print(maxi)