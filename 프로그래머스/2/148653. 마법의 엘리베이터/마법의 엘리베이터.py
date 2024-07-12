def solution(storey):
    answer = 0
    
    while storey:
        temp = storey % 10 
        if temp > 5:
            answer += (10 - temp)
            storey += 10
        elif temp < 5:
            answer += temp
        else:
            if (storey // 10) % 10 >= 5:
                answer += (10 - temp)
                storey += 10
            else:
                answer += temp
        storey //= 10
    
    return answer