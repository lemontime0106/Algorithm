def solution(dartResult):
    answer = []
    temp = ""
    
    for i in dartResult:
        if i.isdigit():
            temp += i
        elif i.isalpha():
            temp = int(temp)
            if i == "S":
                answer.append(temp)
            elif i == "D":
                answer.append(temp ** 2)
            elif i == "T":
                answer.append(temp ** 3)
            temp = ""
        elif i == "*":
            if len(answer) > 1:
                answer[-1] *= 2
                answer[-2] *= 2
            else:
                answer[-1] *= 2
        elif i == "#":
            answer[-1] *= -1
                
    return sum(answer)