def solution(x):
    str_x = str(x)
    
    temp = 0
    
    for i in str_x:
        temp += int(i)
    
    if x % temp:
        return False
    else:
        return True
    
