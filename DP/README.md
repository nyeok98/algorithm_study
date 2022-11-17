### 1149 - RGB거리
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
