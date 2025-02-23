def solution(answers):
    answer = []
    
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    na, nb, nc = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == a[i]:
            na += 1
        
        if answers[i] == b[i]:
            nb += 1
        
        if answers[i] == c[i]:
            nc += 1
        
    if na == max(na, nb, nc):
        answer.append(1)
    if nb == max(na, nb, nc):
        answer.append(2)
    if nc == max(na, nb, nc):
        answer.append(3)
    
    answer.sort()    
    
    return answer