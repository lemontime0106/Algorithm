def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
        
    for p in photo:
        temp = 0
        for i in p:
            if i in score:
                temp += score[i]
            else:
                continue
        answer.append(temp)
    
    return answer