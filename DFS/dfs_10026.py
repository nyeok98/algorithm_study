import sys
sys.setrecursionlimit(10001)

n = int(input())

graph = []
for i in range(n):
    graph.append(list(input()))


def dfs_a(x, y, alpha):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] != alpha:
        return False
    if visited[x][y] == 0:
        visited[x][y] = 1
        dfs_a(x-1, y, alpha)
        dfs_a(x+1, y, alpha)
        dfs_a(x, y+1, alpha)
        dfs_a(x, y-1, alpha)
        return True
    return False


def dfs_b(x, y, alpha):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if alpha == 'B':
        if graph[x][y] != 'B':
            return False
    else:
        if graph[x][y] == 'B':
            return False

    if visited[x][y] == 0:
        visited[x][y] = 1
        dfs_b(x-1, y, alpha)
        dfs_b(x+1, y, alpha)
        dfs_b(x, y+1, alpha)
        dfs_b(x, y-1, alpha)
        return True
    return False


group_a = 0
group_b = 0

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dfs_a(i, j, graph[i][j]) == True:
            group_a += 1

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dfs_b(i, j, graph[i][j]) == True:
            group_b += 1


print(group_a, group_b)
