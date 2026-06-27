def solution(d, budget):
    answer = 0
    
    d.sort()
    temp = 0
    
    for i in range(len(d)):
        temp += d[i]
        if temp < budget:
            answer += 1
            continue
        elif temp == budget:
            answer += 1
            return answer
        else:
            return answer
    return answer
