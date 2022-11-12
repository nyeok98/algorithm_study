import heapq
import sys
input = sys.stdin.readline
INF = int(1e10)+1
# 입력의 엣지케이스 크기에 따라 INF도 충분하지 않을 때가 있다.
# 이경우에는 예를 들어 정상적으로 접근이 가능하더라도 10만개의 노드 당 비용이 10만이라면 result가 내가 자주쓰는 INF를 이미 초과하여 -1이 출력될 것이기 때문

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

blocked = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if blocked[i[0]] and i[0] < n-1:
                cost = INF
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(0)

result = distance[n-1]
if result >= INF:
    print(-1)
else:
    print(result)
