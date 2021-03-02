import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    m = int(input())
    if m == 0:
        if q:
            print(-(heapq.heappop(q)))
        else:
            print(0)
    else:
        heapq.heappush(q, -m)