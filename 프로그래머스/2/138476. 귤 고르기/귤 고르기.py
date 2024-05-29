def solution(k, tangerine):
    number = {}
    
    for i in tangerine:
        if i not in number:
            number[i] = 1
        else:
            number[i] += 1
    
    sorted_number = sorted(number.values(), reverse=True)
    
    answer = 0
    cnt = 0
    
    for count in sorted_number:
        cnt += count
        answer += 1
        if cnt >= k:
            break
    
    return answer