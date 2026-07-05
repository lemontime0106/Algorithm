def solution(seoul):
    temp = 0
    
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            temp = i
            break
    
    return f"김서방은 {temp}에 있다"