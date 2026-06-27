def solution(survey, choices):
    answer = ''
    
    score = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0
    }
    
    N = len(survey)
    
    for i in range(N):
        s, choice = survey[i], choices[i]
        
        if choice < 4:
            score[s[0]] += 4 - choice
        elif choice > 4:
            score[s[1]] += choice - 4
            
    for a, b in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        if score[a] >= score[b]:
            answer += a
        else:
            answer += b
        
    return answer