from collections import deque
import sys
sys.setrecursionlimit(100000)
#Recursion error로 인한 limit 변

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

isVisited = [[False]*n for _ in range(n)]
#단순 방문 여부처럼 나뉘는게 아니라 높이에 따른 차이이므로 visiterd 리스트를 따로 만들어준다.
height = 0
#현재 dfs를 실행할 때의 높이기준
def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if isVisited[x][y]:
        return False
    if graph[x][y] >= height:
        isVisited[x][y] = True
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

highest = 0
#시작할 최대 높이를 찾기 위한 과정
for i in range(n):
    for j in range(n):
        highest = max(highest, graph[i][j])

count_list = []
#측정한 최대높이로부터 모든 높이별 홍수를 파악하기 위해 하나씩 줄여 준다.
for k in range(highest, -1, -1):
    height = k
    count = 0
    for i in range(n):
        for j in range(n):
            if isVisited[i][j]:
                continue
            if dfs(i, j):
                count += 1
    count_list.append(count)
    isVisited = [[False]*n for _ in range(n)]
    #방문여부 초기화

print(max(count_list))