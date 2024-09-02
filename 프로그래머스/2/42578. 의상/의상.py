def solution(clothes):
    closet = {}
    for a, b in clothes:
        if b in closet.keys():
            closet[b] += [a]
        else:
            closet[b] = [a]
    
    answer = 1
    for a, b in closet.items():
        answer *= (len(b) + 1)
    
    return answer - 1