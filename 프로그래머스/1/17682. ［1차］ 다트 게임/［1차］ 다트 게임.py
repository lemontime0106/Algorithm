def solution(dartResult):
    answer = []
    dartResult = list(dartResult)
    
    while dartResult:
        score = ""
        
        temp = dartResult.pop(0)
        
        while True:
            score += temp
            
            if not dartResult:
                break
            
            if dartResult[0].isdigit():
                temp = dartResult.pop(0)
            else:
                break
            
        score = int(score)
        
        option = dartResult.pop(0)
        
        if option == "S":
            score = score ** 1
        elif option == "D":
            score = score ** 2
        elif option == "T":
            score = score ** 3
        
        if dartResult and dartResult[0] in ["*", "#"]:
            bonus = dartResult.pop(0)
            
            if bonus == "*":
                score *= 2
                if answer:
                    answer[-1] *= 2
            else:
                score *= -1
        
        answer.append(score)
    
    return sum(answer)