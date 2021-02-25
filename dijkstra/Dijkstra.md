# 다익스트라(Dijkstra)✍️

### 다익스트라 알고리즘은 최단 경로를 구하는 효과적인 알고리즘이다.
##### 출발점과 끝점이 있다는 데에서 플로이드-와샬과 차이점이 있다.
###### 플로이드-와샬과은 모든 노드에서 모든 노드까지의 최소비용을 구함.
##### 문제 중 언뜻 보면 BFS, DFS로 풀어야할 것 같은 경우들이 있는데 햇갈리지 말자!

***

##### 출발 노드와 탐색하는 노드에서 최소거리(비용)을 갖는 노드를 탐색해야 한다는 점에서 우선순위 큐(Priority Queue)
##### 즉, 힙(Heap) 구조를 이용하면 효과적으로 구현할 수 있다. 이 때 힙은 최소 힙(Minimum Heap)이다.
##### 🔽 아래는 힙을 이용한 다익스트라 알고리즘의 구현부

```python
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
```
###### 이 때 Python의 힙 구조에 저장되는 비용-노드번호와 통상 문제에서 제시되는 노드번호-비용 구조가 동일하지 않음으로 햇갈리지 않도록 한다.
