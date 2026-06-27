def solution(participant, completion):
    temp = dict()
    
    for i in participant:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] += 1
            
    for i in completion:
        temp[i] -= 1
    
    for i in temp:
        if temp[i] == 1:
            return i