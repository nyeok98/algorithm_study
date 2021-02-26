n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

zero = 0
one = 0

def divide(x, y, type):
    global zero, one
    total = type**2
    count_zero = 0
    count_one = 0
    for i in range(x, x+type):
        for j in range(y, y+type):
            if graph[i][j] == 0:
                count_zero += 1
            else:
                count_one += 1
    if count_zero == total:
        zero += 1
    elif count_one == total:
        one += 1
    else:
        divide(x, y, type//2)
        divide(x, y+(type//2), type//2)
        divide(x+(type//2), y, type//2)
        divide(x+(type//2), y+(type//2), type//2)

divide(0, 0, n)

print(zero)
print(one)