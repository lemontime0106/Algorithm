def solution(n):
    graph = [[0] * (i+1) for i in range(n)]
    
    direct = [(1, 0), (0, 1), (-1, -1)]
    
    x, y = -1, 0
    num = 1
    direction = 0
    
    for i in range(n, 0, -1):
        for _ in range(i):
            x += direct[direction][0]
            y += direct[direction][1]
            graph[x][y] = num
            num += 1
        
        direction = (direction + 1) % 3
        
    answer = []
    for row in graph:
        answer.extend(row)
    
    return answer