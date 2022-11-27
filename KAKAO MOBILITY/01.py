def solution(flowers):
    days = [0] * 13
    answer = 0
    for i in flowers:
        for j in range(i[0], i[1]+1):
            days[j] += 1
    for i in range(1, 13):
        if days[i] >= 1:
            answer += 1
    print(days)
    return answer


print(solution([[2, 5], [3, 7], [10, 11]]))
