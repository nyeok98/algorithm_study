import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []

def absolute(n):
    if n == 0:
        if q:
            temp = heapq.heappop(q)
            if temp[1] == 1:
                print(temp[0])
            else:
                print(-temp[0])
        else:
            print(0)
    else:
        if n >= 0:
            heapq.heappush(q,(n, 1))
        else:
            heapq.heappush(q,(-n, 0))

for _ in range(n):
    absolute(int(input()))