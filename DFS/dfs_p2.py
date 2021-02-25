def dfs(x, y):
    if x<=-1 or x>=h or y<=-1 or y>=w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y+1)
        return True
    return False

graph = []
w, h = map(int, input().split())

while not (w==0 and h==0):
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1
    print(result)
    w, h = map(int, input().split())
