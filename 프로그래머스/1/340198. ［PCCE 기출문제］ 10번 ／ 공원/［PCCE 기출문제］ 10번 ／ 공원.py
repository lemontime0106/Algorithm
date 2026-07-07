def solution(mats, park):
    mats.sort(reverse=True)
    
    N = len(park)
    M = len(park[0])
    
    for size in mats:
        for i in range(N - size + 1):
            for j in range(M - size + 1):
                flag = True
                
                for x in range(i, i+size):
                    for y in range(j, j+size):
                        if park[x][y] != "-1":
                            flag = False
                            break
                    if not flag:
                        break
                        
                if flag:
                    return size
    return -1