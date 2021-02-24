n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(int(input()))

d = [10001]*(m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우, 없어도 결과는 정상 출력됨.
            d[j] = min(d[j], d[j-array[i]]+1)
            #j-array[i]가 뜻하는 것은 array에 들어있어야하는 화폐단위만큼 이전으로 간 것에 +1만큼의 화폐가 더 필요하다는 뜻이다.

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])