n = int(input())

data = list(map(int, input().split()))

d = [0]*101
d[1] = data[0]
d[2] = data[1]

for i in range(3, n):
    d[i] = max(d[i-1], d[i-2] + data[i-1])

print(d[n-1])