from collections import deque
import sys
sys.setrecursionlimit(100000)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

isVisited = [[False]*n for _ in range(n)]

height = 0

def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if isVisited[x][y]:
        return False
    if graph[x][y] >= height:
        isVisited[x][y] = True
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

highest = 0
for i in range(n):
    for j in range(n):
        highest = max(highest, graph[i][j])

count_list = []
for k in range(highest, -1, -1):
    height = k
    count = 0
    for i in range(n):
        for j in range(n):
            if isVisited[i][j]:
                continue
            if dfs(i, j):
                count += 1
    count_list.append(count)
    isVisited = [[False]*n for _ in range(n)]

print(max(count_list))