def solution(k, score):
    answer = []
    temp = []
    
    for i in range(len(score)):
        if len(temp) < k:
            temp.append(score[i])
            temp.sort(reverse=True)
        
        else:
            if temp[-1] < score[i]:
                temp.pop()
                temp.append(score[i])
                temp.sort(reverse=True)
        
        answer.append(temp[-1])
        
    return answer