import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance_start = [INF] * (n+1)
distance_e1 = [INF] * (n+1)
distance_e2 = [INF] * (n+1)
special = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

e1, e2 = map(int, input().split())


def dijkstra(distance, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(distance_start, 1)
dijkstra(distance_e1, e1)
dijkstra(distance_e2, e2)

result = min(distance_start[e1]+distance_e1[e2]+distance_e2[n],
             distance_start[e2]+distance_e2[e1]+distance_e1[n])

if result >= INF:  # 전체 합이 INF보다 당연히 커질 수 있음
    print(-1)
else:
    print(result)
