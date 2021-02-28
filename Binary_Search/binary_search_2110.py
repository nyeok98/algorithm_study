import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

min = 1
max = house[-1] - house[0]
result = 0

while min <= max:
    mid = (max + min) // 2
    hub = 1
    now = house[0]
    for i in range(1, n):
        if house[i] - now >= mid:
            hub += 1
            now = house[i]
    if hub >= c:
        min = mid+1
        result = mid
    else:
        max = mid-1

print(result)
