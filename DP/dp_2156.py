n = int(input())

graph = [[0] for _ in range(n+1)]
data = [0]

for _ in range(n):
    data.append(int(input()))

graph[1] = data[1]


for i in range(3,n+1):
    graph[i] = max(data[i] + graph[i-4], data[i] + graph[i-1], data[i] + )

print(graph[n])
