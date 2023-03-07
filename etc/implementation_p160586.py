def solution(keymap, targets):
    answer = []
    dic = {'A':-1, 'B':-1, 'C':-1, 'D':-1, 'E':-1, 'F':-1, 'G':-1, 'H':-1, 'I':-1, 'J':-1, 'K':-1, 'L':-1, 'M':-1, 'N':-1,'O':-1, 'P':-1, 'Q':-1, 'R':-1, 'S':-1, 'T':-1, 'U':-1, 'V':-1, 'W':-1, 'X':-1, 'Y':-1, 'Z':-1}
    for key in keymap:
        index = 1
        for i in key:
            if dic[i] == -1:
                dic[i] = index
            else:
                if dic[i] > index:
                    dic[i] = index
            index += 1
    
    for target in targets:
        count = 0
        flag = False
        for j in target:
            if dic[j] == -1:
                flag = True
                break
            count += dic[j]
        if flag or count == 0:
            answer.append(-1)
        else:
            answer.append(count)
                
    return answer