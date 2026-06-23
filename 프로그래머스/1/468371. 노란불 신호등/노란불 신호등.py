def is_yellow(time, green, yellow, red):
    cycle = green + yellow + red
    pos = (time - 1) % cycle
    
    return green <= pos < green + yellow

def solution(signals):
    answer = 0
    
    temp = [sum(signal) for signal in signals]
    
    max_num = 1
    for i in temp:
        max_num *= i
        
    for i in range(1, max_num):
        flag = True
        
        for g, y, r in signals:
            if not is_yellow(i, g, y, r):
                flag = False
                break
                
        if flag:
            return i
    
    return -1