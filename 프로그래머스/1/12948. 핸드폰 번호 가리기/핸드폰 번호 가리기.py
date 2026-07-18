def solution(phone_number):
    answer = ''
    
    len_number = len(phone_number)
    
    for i in range(len_number):
        if i < len_number-4:
            answer += "*"
        else:
            answer += str(phone_number[i])
    
    return answer