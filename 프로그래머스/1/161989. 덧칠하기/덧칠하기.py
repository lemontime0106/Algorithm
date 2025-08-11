

def solution(n, m, section):
    answer = 0
    
    lst = [True] * n
    for i in section:
        lst[i-1] = False
        
    i = 0
    while i < n:
        if not lst[i]:
            for j in range(m):
                if i + j >= n:
                    break        
                lst[i + j] = True
            answer += 1
            i += m
        else:
            i += 1
        
    return answer