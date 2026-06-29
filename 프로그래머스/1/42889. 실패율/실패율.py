def solution(N, stages):
    answer = []
    
    temp = dict()
    
    user = len(stages)
    
    for i in range(1, N+1):
        fail = stages.count(i)
        
        if user == 0:
            rate = 0
        else:
            rate = fail / user
        
        temp[i] = rate
        user -= fail
    
    answer = sorted(temp, key=lambda x: (-temp[x], x))
    
    return answer