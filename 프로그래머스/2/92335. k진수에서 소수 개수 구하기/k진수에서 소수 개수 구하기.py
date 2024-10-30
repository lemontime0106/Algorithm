import math

def solution(n, k):
    word = ""
    
    while n:
        word = str(n % k) + word
        n //= k
        
    word = word.split("0")
    
    answer = 0
    for w in word:
        if not w:
            continue
        num = int(w)
        
        if num < 2:
            continue
        
        prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            answer += 1
    
    return answer
