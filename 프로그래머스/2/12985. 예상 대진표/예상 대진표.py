def solution(n, a, b):
    answer = 0
    
    while True:
        if (a + 1) // 2 == (b + 1) // 2:
            answer += 1
            break

        if a % 2 == 0:
            a //= 2
        else:
            a = a // 2 + 1
        
        if b % 2 == 0:
            b //= 2
        else:
            b = b // 2 + 1
        
        answer += 1

    return answer