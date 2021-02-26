cnt = 0

while 1:
    l, p, v = map(int, input().split())
    if l+p+v == 0:
        break
    cnt += 1
    day = v//p
    day = day*l
    last = v%p
    if last >= l:
        day += l
    else:
        day += last


    print("Case %d: %d" %(cnt, day))