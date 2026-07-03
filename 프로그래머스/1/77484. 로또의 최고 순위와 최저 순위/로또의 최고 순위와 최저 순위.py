def solution(lottos, win_nums):
    zero = lottos.count(0)
    match = 0
    
    for n in lottos:
        if n in win_nums:
            match += 1
    
    def rank(cnt):
        if cnt >= 6:
            return 1
        elif cnt == 5:
            return 2
        elif cnt == 4:
            return 3
        elif cnt == 3:
            return 4
        elif cnt == 2:
            return 5
        else:
            return 6
    
    best = rank(match + zero)
    worst = rank(match)
    
    return [best, worst]