def solution(s, skip, index):
    answer = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for i in list(skip):
        alpha = alpha.replace(i, "")
        
    for a in s:
        answer += alpha[(alpha.find(a) + index) % len(alpha)]
    return answer