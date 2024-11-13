def solution(mats, park):
    answer = 0
    mats.sort(reverse=True)
    
    R = len(park)
    C = len(park[0])
    
    def check(x, y, m):
        for i in range(x, x+m):
            for j in range(y, y+m):
                if i < R and j < C:
                    if park[i][j] != "-1":
                        return False
                else:
                    return False
        return True
                         
    for mat in mats:
        for i in range(R):
            for j in range(C):
                if check(i, j, mat):
                    return mat
    
    return -1