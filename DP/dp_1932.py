n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

d = [[0]*(n) for _ in range(n)]
d[0][0] = graph[0][0]

for i in range(1,n):
    for j in range(n):
        if j>i:
            continue
        if j==0:
            d[i][j] = d[i-1][j] + graph[i][j]
        elif j==i:
            d[i][j] = d[i-1][j-1] + graph[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + graph[i][j]

print(max(d[n-1]))