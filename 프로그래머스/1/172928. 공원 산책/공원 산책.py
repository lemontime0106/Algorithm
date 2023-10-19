def solution(park, routes):
    H = len(park)
    W = len(park[0])
    x, y = 0, 0
    
    direct = {
        'E' : (0, 1), 
        'W' : (0, -1),
        'S' : (1, 0),
        'N' : (-1, 0),
    }
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x = i
                y = j
    
    for route in routes:
        d, l = route.split()
        l = int(l)
        flag = True
        nx = x
        ny = y
        for k in range(1, l+1):
            nx += direct[d][0]
            ny += direct[d][1]
            if nx < 0 or nx >= H or ny < 0 or ny >= W or park[nx][ny] == 'X':
                flag = False
                break
        if flag:
            x += direct[d][0] * l
            y += direct[d][1] * l
        
    answer = [x, y]
    print(answer)
    return answer
