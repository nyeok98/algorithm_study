import sys
input = sys.stdin.readline


def solution(id_list, k):
    coupon_count = {}
    client_id = []
    for i in id_list:
        day_client = []
        client_id = i.split()
        for j in client_id:
            if j in day_client:
                continue
            else:
                day_client.append(j)
            if j in coupon_count:
                if coupon_count[j] < k:
                    coupon_count[j] += 1
            else:
                coupon_count[j] = 1

    answer = sum(coupon_count.values())

    return answer
