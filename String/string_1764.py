"""
1764번 - 듣보잡
입력받는 수가 500,000이 넘어가므로 단순 이중 반복으로 하면 250,000,000,000이므로
이분 탐색을 이용하는 것이 적절하다.
"""
n, m = map(int, input().split())
n_list = []
m_list = []
result = []

for _ in range(n):
    n_list.append(input())

for _ in range(m):
    m_list.append(input())

# 이분 탐색을 진행하기 위해 탐색 대상이 될 리스트를 순서대로 정렬
m_list.sort()
# 시작점과 끝점을 잡는다.
start = 0
end = len(m_list)-1

def binary_search(k, start, end):
    # 이상한 이분탐색 사용하지말고 정석에 따르자.
    while start <= end:
        mid = (start + end) // 2
        if k == m_list[mid]:
            result.append(k)
            return
        elif k > m_list[mid]:
            start = mid+1
        else:
            end = mid-1

for case in n_list:
    binary_search(case, start, end)

result.sort()
print(len(result))
for k in result:
    print(k)