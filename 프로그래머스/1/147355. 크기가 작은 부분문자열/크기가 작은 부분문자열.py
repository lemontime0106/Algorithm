def solution(t, p):
    answer = 0
    
    T = len(t)
    P = len(p)
    num_p = int(p)
    
    for i in range(T-P+1):
        num = ""
        
        for j in range(i, i+P):
            num += t[j]
            
        if int(num) <= num_p:
            answer += 1
    
    return answer