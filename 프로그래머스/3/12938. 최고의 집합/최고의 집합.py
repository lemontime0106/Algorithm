def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    num = s // n
    remain = s % n
    
    for i in range(n):
        answer.append(num)
        
    if remain != 0:
        for i in range(n):
            answer[i] += 1
            remain -= 1
            if remain == 0:
                break
    answer.sort()
    
    return answer