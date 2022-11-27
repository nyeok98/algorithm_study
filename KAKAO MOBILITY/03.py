import copy


def isSerial(prev_time, new_time):
    y = new_time[0] - prev_time[0]
    m = new_time[1] - prev_time[1]
    d = new_time[2] - prev_time[2]
    if y == 1 and m == -11 and d == -29:
        return True
    elif y == 0 and m == 1 and d == -29:
        return True
    elif y == 0 and m == 0 and (d == 1 or d == 0):
        return True
    else:
        return False


def get_next_time(prev_time, time):
    next_time = prev_time.copy()
    for i in range(5, 0, -1):
        next_time[i] += time[i]
        if i == 5 and next_time[i] >= 60:
            next_time[i-1] += 1
            next_time[i] -= 60
        elif i == 4 and next_time[i] >= 60:
            next_time[i-1] += 1
            next_time[i] -= 60
        elif i == 3 and next_time[i] >= 24:
            next_time[i-1] += 1
            next_time[i] -= 24
        elif i == 2 and next_time[i] >= 30:
            next_time[i-1] += 1
            next_time[i] -= 30
        elif i == 1 and next_time[i] >= 12:
            next_time[i-1] += 1
            next_time[i] -= 12

    return next_time


def day_gap(last_time, first_time):
    day = 0
    day += (last_time[0] - first_time[0]) * 360
    day += (last_time[1] - first_time[1]) * 30
    day += last_time[2] - first_time[2]
    return day


def solution(s, times):
    first_time = []
    prev_time = []
    isSerial_answer = True

    first_time = list(map(int, s.split(':')))  # 토큰 단위 분절된 입력
    prev_time = first_time.copy()
    times_d = []  # 입력을 토큰으로 분할시킨 배열

    for time in times:
        base = [0000, 00]
        times_d.append(base + list(map(int, time.split(':'))))

    for time in times_d:
        next_time = get_next_time(prev_time, time)
        if (isSerial_answer):
            isSerial_answer = isSerial(prev_time, next_time)
        prev_time = next_time.copy()

    # 답 완성
    answer = [0, 0]
    gap = day_gap(prev_time, first_time)

    if isSerial_answer:
        answer[0] = 1
    answer[1] = gap + 1

    return answer
