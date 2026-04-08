while True:
    n = input().strip()
    
    if n == '0':
        break
    
    width = 2
    
    for ch in n:
        if ch == '1':
            width += 2
        elif ch == '0':
            width += 4
        else:
            width += 3
    
    width += len(n) - 1
    
    print(width)