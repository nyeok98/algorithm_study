n = int(input())

d = [0] * 30000

d[1] = 0
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 1

for i in range(6, n+1):
    if i % 5 == 0:
        d[i] = min(d[i-1], d[i//5]) + 1
    elif i % 3 == 0:
        d[i] = min(d[i-1], d[i//3]) + 1
    elif i % 2 == 0:
        d[i] = min(d[i-1], d[i//2]) + 1
    else:
        d[i] = d[i-1] + 1

print(d[n])
