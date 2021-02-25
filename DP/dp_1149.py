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