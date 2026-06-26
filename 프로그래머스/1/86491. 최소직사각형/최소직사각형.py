def solution(sizes):
    answer = 0
    
    big = []
    small = []
    
    for a, b in sizes:
        if a > b:
            big.append(a)
            small.append(b)
        else:
            big.append(b)
            small.append(a)
    
    return max(big) * max(small)