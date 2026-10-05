def dfs(n, t, i, v):
    global answer
    
    if i == len(n) and v == t:
        answer += 1
        return
    
    if i == len(n):
        return
    
    dfs(n, t, i+1, v + n[i])
    dfs(n, t, i+1, v - n[i])

def solution(numbers, target):
    global answer 
    answer = 0
    
    dfs(numbers, target, 0, 0)
    
    return answer