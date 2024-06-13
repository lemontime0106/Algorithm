def solution(s):
    answer = []
    
    word = list(s)
    position = {}
    for i in range(len(word)):
        if word[i] not in position:
            position[word[i]] = i
            answer.append(-1)
        else:
            answer.append((i - position[word[i]]))
            position[word[i]] = i
        
    return answer