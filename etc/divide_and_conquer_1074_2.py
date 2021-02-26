n, r, c = map(int, input().split())
size = 2**n
start = 0
start_x, start_y = 0, 0

def set_start(r, c, n):
    global start, start_x, start_y
    if n == 0:
        if r != start_x:
            start += 1
        if c != start_y:
            start += 2
        return
    half_x = start_x+2**(n-1)
    half_y = start_y+2**(n-1)
    base = 2**((2*n)-2)
    if r < half_x:
        if c >= half_y:
            start_y = half_y
            start += base
    else:
        if c < half_y:
            start_x = half_x
            start += base*2
        else:
            start_x = half_x
            start_y = half_y
            start += base*3
    set_start(r, c, n-1)

set_start(r, c, n)

print(start)