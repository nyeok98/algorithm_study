import heapq

n = int(input())
q = []
m = []

for _ in range(n):
    m.append(int(input()))

for i in m:
    if i == 0:
        temp = 0
        if q:
            temp = heapq.heappop(q)
        print(temp)
    else:
        heapq.heappush(q, i)