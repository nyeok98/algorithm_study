# ✍️BFS(너비 우선 탐색)

#### BFS(너비우선 탐색)는 DFS(깊이 우선 탐색)와 짝을 이룬다.
#### 현재까지 파악한 바로는 행렬에서 전염성이 있는 무언가에 의한 단계별 판단을 이루어야 할 경우 쓰임.

***

```python
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
```

##### 이처럼 주로 행렬을 탐색하는 과정에서
##### __while___,___queue__ 를 통해 해결하는 방식.
##### 시작점을 제일 먼저 큐에 삽입 후, 인접한 노드가 조건에 부합한다면 마찬가지로 큐에 삽입
##### 🎈DFS와의 차이점: dfs는 스택을 이용하거나, 위와 같이 조건을 만족한 노드에서 재귀식으로 깊게 들어가는 데에 반해, bfs는 큐에 들어온 순서대로 처리한다.
