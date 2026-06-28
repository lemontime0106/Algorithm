def solution(n, words):
    answer = []

    user = dict()
    word = dict()
    N = len(words)
    
    for i in range(1, n+1):
        user[i] = 1
    
    for i in range(N):
        w = words[i]
        person = (i % n) + 1
        
        if w in word:
            return [person, user[person]]
        
        if i > 0 and words[i-1][-1] != w[0]:
            return [person, user[person]]
        
        word[w] = 1
        
        user[person] += 1
            

    return [0, 0]