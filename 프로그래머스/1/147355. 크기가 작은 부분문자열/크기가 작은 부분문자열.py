def solution(t, p):
    answer = 0
    
    T = len(t)
    P = len(p)
    
    for i in range(T-P+1):
        num = ""
        for j in range(P):
            num += t[i+j]
        
        if (int(p) >= int(num)):
            answer += 1
            
    return answer