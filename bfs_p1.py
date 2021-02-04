from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = -1

for i in range(m):
    j, k = map(int, input().split())
    graph[j].append(k)
    graph[k].append(j)

def bfs(graph, start, visited):
    global result
    queue = deque([start])
    visited[start] = True
    while queue:
        result += 1
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
print(result)