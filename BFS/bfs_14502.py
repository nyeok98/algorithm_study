from collections import deque
import itertools
import copy

n, m = map(int, input().split())
graph = []
origin_queue = deque()
zero_queue = deque()

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(wall):
    temp_graph = copy.deepcopy(graph)
    temp_queue = copy.deepcopy(origin_queue)
    for i, j in wall:
        temp_graph[i][j] = 1
    while temp_queue:
        x, y = temp_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if temp_graph[nx][ny] == 1:
                continue
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                temp_queue.append((nx, ny))
    count = 0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                count += 1
    return count

def pick_wall():
    data = list(itertools.combinations(zero_queue, 3))
    return data

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            origin_queue.append((i, j))
        elif graph[i][j] == 0:
            zero_queue.append((i, j))

safe_list = []
data = pick_wall()
for i in data:
    safe_list.append(bfs(i))

print(max(safe_list))
