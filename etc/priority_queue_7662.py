import heapq
import sys
from heapq import nlargest
input = sys.stdin.readline

q = []
result = []
n = int(input())

for _ in range(n):
    m = int(input())
    for _ in range(m):
        temp = input().split()
        if temp[0] == 'I':
            heapq.heappush(q, int(temp[1]))
        else:
            if int(temp[1]) == 1:
                if q:
                    q.pop(q.index(nlargest(1,q)[0]))
            else:
                if q:
                    heapq.heappop(q)

    if not q:
        result.append("EMPTY")
    else:
        maxi = q.pop(q.index(nlargest(1,q)[0]))
        mini = heapq.heappop(q)
        result.append((maxi, mini))

for i in range(n):
    if result[i] == "EMPTY":
        print("EMPTY")
    else:
        print(result[1][0], result[1][1])