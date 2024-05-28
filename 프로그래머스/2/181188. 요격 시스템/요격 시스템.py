def solution(targets):
    temp = sorted(targets, key = lambda x: (x[1],x[0]))
    shoot = 1
    
    change = 0
    
    for i in range(len(targets)):
        if i == 0:
            change = temp[i][1]
        if change <= temp[i][0]:
            change = temp[i][1]
            shoot += 1
    
    return shoot