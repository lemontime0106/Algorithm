def solution(n, w, num):
    answer = 0
    floor = n // w + 1
    MAP = []
    
    for i in range(floor):
        temp = []
        for j in range(1, w+1):
            if i * w + j <= n:
                temp.append(i * w + j)
            else:
                temp.append(0)
        
        if i % 2 == 1:
            MAP.append(temp[::-1])
        else:
            MAP.append(temp)
            
    for i in range(floor):
        for j in range(w):
            if MAP[i][j] == num:
                for k in range(floor):
                    answer += 1
                    i += 1
                    if i >= floor:
                        return answer
                    if MAP[i][j] == 0:
                        return answer
    
    return answer