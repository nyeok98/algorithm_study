# ✍️DP(Dynamic Programming)
##### 처음 문제를 마주쳤을 때, 다이나믹 프로그래밍과 분할정복을 햇갈리지 말아야 한다.
- 다이나믹 프로그래밍 - 문제들이 서로 영향을 미치고 있다(ex. 피보나치 수열)
- 분할정복 - 문제가 작은 단위로 나뉘어 질 뿐 서로 영향을 미치지 않는다(ex. 퀵 정렬)

***

</br>

## 💡다이나믹 프로그래밍의 두 종류
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

#### 📌가능한 Bottom-Up 방식을 떠올리는 것이 좋다.


***

#### 백준 1149 RGB거리를 풀면서
###### 내게 조금 특별한 문제, 알고리즘을 1년가까이 놓기 직전 마지막으로 공부하던 부분을 다시 따라잡았고,
###### 더 위에서 보며 문제를 해결할 수 있었다.

###### 이러한 감회 이외에도, 꼭 기억해야할 점.

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
###### 처음에 DP로 풀어나가기가 너무 막막해서 그리디 형식으로 풀었다.
###### 이처럼 DP는 자칫 잘못 생각하면 그리디로 풀어도 되지 않나...하는 오류는 낳는다.

###### 그러나, 그리디로 푼다면 1번 집 최소, 2번 집 최소의 경우를 선택하고 3번 집 최소를 선택하게 되는데 이것보다
###### 1번 집 최소, 2번집 2번째로 최소, 3번집 최소 등의 경우의 수를 선택하면 더 최소인 결과값을 얻을 수 있게 된다.

###### 따라서 3단 리스트가 자칫 복잡해보여도 DP임을 파악한다면 주저 없이 도전할 것.
