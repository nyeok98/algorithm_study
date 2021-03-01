import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lesson = list(map(int, input().split()))
total = sum(lesson)
result = 0

start = 0
end = total

while start <= end:
    mid = (start + end) / 2
    temp_sum = 0
    lay = 0
    for i in range(0, n-1):
        temp_sum += lesson[i]
        if temp_sum + lesson[i+1] >= mid:
            lay += 1
            temp_sum = 0

    if lay >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
