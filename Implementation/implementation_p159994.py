from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    q1 = deque(cards1)
    q2 = deque(cards2)
    result = []
    
    for word in goal:
        if q1 and q1[0] == word:
            result.append(q1.popleft())
        elif q2 and q2[0] == word:
            result.append(q2.popleft())
            
    if result == goal:
        return 'Yes'
    else:
        return 'No'