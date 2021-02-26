import time
start = time.time()

n, r, c = map(int, input().split())
size = 2**n
array = [[0]*size for _ in range(size)]
count = 0

def z_conquer(x, y, type):
    global count
    if x > size-1 or y > size-1:
        return
    if type == 0:
        array[x][y] = count
        array[x][y+1] = count+1
        array[x+1][y] = count+2
        array[x+1][y+1] = count+3
        count += 4
        return
    z_conquer(x, y, type-1)
    z_conquer(x, y+(2**type), type-1)
    z_conquer(x+(2**type), y, type-1)
    z_conquer(x+(2**type), y+(2**type), type-1)

z_conquer(0, 0, n)

print(array[r][c])
print(time.time()-start)