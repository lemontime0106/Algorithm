def solution(scores):
    answer = 1
    my_a, my_b = scores[0]
    my_score = my_a + my_b
    
    scores.sort(key = lambda x: (-x[0], x[1]))
    max_b = 0

    for a, b in scores:
        if my_a < a and my_b < b:
            return -1
        
        if b >= max_b:
            max_b = b
            if a + b > my_score:
                answer += 1
                
    return answer