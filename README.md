## 🖥 알고리즘을 공부하는 공간 ✍️
#### 고전이 고전인 이유는, 결코 진리에 가깝도록 불변함이 수많은 반례에 의해 무너지지 않았음이다.
#### 기본부터 충실하게, 우직하게, 한 걸음씩 내딛어 본다🐮
</br>
</br>
</br>

### 📍목차
****
[BFS(너비 우선 탐색)](#bfs)

[DP(다이나믹 프로그래밍)](#dp)

[Dijkstra(다익스트라)](#dijkstra)


</br>
</br>
</br>

# BFS

> BFS(너비우선 탐색)는 DFS(깊이 우선 탐색)와 짝을 이룬다.
> 현재까지 파악한 바로는 행렬에서 전염성이 있는 무언가에 의한 단계별 판단을 이루어야 할 경우 쓰임.

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

****
</br>
</br>
</br>
</br>

# DP
> 처음 문제를 마주쳤을 때, 다이나믹 프로그래밍과 분할정복을 햇갈리지 말아야 한다.
> - 다이나믹 프로그래밍 - 문제들이 서로 영향을 미치고 있다(ex. 피보나치 수열)
> - 분할정복 - 문제가 작은 단위로 나뉘어 질 뿐 서로 영향을 미치지 않는다(ex. 퀵 정렬)

##### 💡다이나믹 프로그래밍의 두 종류
- Top-Down(주로 메모이제이션)

```python
d = [0]*100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
```
</br>

- Bottom-Up(주로 반복문 사용)

```python
d = [0]*100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
```

##### 📌가능한 Bottom-Up 방식을 떠올리는 것이 좋다.


***

##### 백준 1149 RGB거리를 풀면서
###### 내게 조금 특별한 문제, 알고리즘을 1년가까이 놓기 직전 마지막으로 공부하던 부분이었는데, 이제야 다시 이 문제를 접하게 되었다.
###### DP에 대한 이해가 더 깊어진 상태로 문제를 해결했다는 느낌이 또렷하게 드는 게 참 좋다.

###### 이러한 감회 이외에도, 꼭 기억해야할 점.

##### [백준 1149번: RGB거리]:(https://www.acmicpc.net/problem/1149)

##### 풀이1

```python
n = int(input())

data = []
d = [0]*(n+1)
for i in range(n):
    data.append(list(map(int, input().split())))

result = min(data[0])
first_index = data[0].index(result)

for i in range(1, n):
    if first_index==0:
        temp = min(data[i][1], data[i][2])
        first_index = data[i].index(temp)
    elif first_index==1:
        temp = min(data[i][0], data[i][2])
        first_index = data[i].index(temp)
    else:
        temp = min(data[i][0], data[i][1])
        first_index = data[i].index(temp)

    result += temp

print(result)
```

##### 풀이2
```python
n = int(input())

data = []
d = [[0]*3 for _ in range(n)]
for i in range(n):
    data.append(list(map(int, input().split())))

d[0][0] = data[0][0]
d[0][1] = data[0][1]
d[0][2] = data[0][2]
d[1][0] = data[1][0] + min(d[0][1], d[0][2])
d[1][1] = data[1][1] + min(d[0][0], d[0][2])
d[1][2] = data[1][2] + min(d[0][0], d[0][1])

for i in range(2, n):
    d[i][0] = data[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = data[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = data[i][2] + min(d[i-1][0], d[i-1][1])

print(min(d[n-1]))
```
###### 처음에 DP로 풀어나가기가 너무 막막하다보니 자연스레 그리디처럼 풀게 되었고 보란듯이 틀렸다.
###### 이처럼 DP는 자칫 잘못 생각하면 그리디로 풀어도 되지 않나...하는 사고회로를 형성하는 것 같다.

###### 그러나, 특히 이 문제의 경우 __당장 이전의 중복만 피하면 된다는 생각을__ 바탕으로 그리디로 푼다면 1번 집 최소, 2번 집 최소의 경우를 선택하고 3번 집 최소를 선택하게 되는데 이것보다 1번 집 최소, 2번집 2번째로 최소, 3번집 최소 등의 경우의 수를 선택하면 더 최소인 결과값을 얻을 수 있는 경우가 발생한다.

###### 이처럼 3단 리스트 등 문제풀이 과정이 자칫 복잡해보여도 DP임을 파악한다면 주저 없이 도전해보자.
***
</br>
</br>
</br>
</br>

# Dijkstra

> 다익스트라 알고리즘은 최단 경로를 구하는 효과적인 알고리즘이다.
> 출발점과 끝점이 있다는 데에서 플로이드-와샬과 차이점이 있다.
> 플로이드-와샬과은 모든 노드에서 모든 노드까지의 최소비용을 구함.
> 문제 중 언뜻 보면 BFS, DFS로 풀어야할 것 같은 경우들이 있는데 햇갈리지 말자!

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
***
</br>
</br>
</br>
</br>
