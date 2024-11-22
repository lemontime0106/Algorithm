def solution(lottos, win_nums):
    answer = []
    
    prize = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    
    contain = 0
    zero = 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1
            continue 
            
        if lotto in win_nums:
            contain += 1
    
    max_rank = zero + contain
    min_rank = contain
    
    answer.append(prize[max_rank])
    answer.append(prize[min_rank])
    
    return answer