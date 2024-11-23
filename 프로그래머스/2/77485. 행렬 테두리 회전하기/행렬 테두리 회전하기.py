def solution(rows, columns, queries):
    answer = []
    
    MAP = [[0] * columns for _ in range(rows)]
    
    num = 1
    for i in range(rows):
        for j in range(columns):
            MAP[i][j] = num
            num += 1
    
    for query in queries:
        x1, y1, x2, y2 = [x - 1 for x in query]
        temp = MAP[x1][y1]
        small = temp
        
        for i in range(x1, x2):
            MAP[i][y1] = MAP[i + 1][y1]
            small = min(small, MAP[i][y1])
        
        for i in range(y1, y2):
            MAP[x2][i] = MAP[x2][i + 1]
            small = min(small, MAP[x2][i])
        
        for i in range(x2, x1, -1):
            MAP[i][y2] = MAP[i - 1][y2]
            small = min(small, MAP[i][y2])
        
        for i in range(y2, y1, -1):
            MAP[x1][i] = MAP[x1][i - 1]
            small = min(small, MAP[x1][i])
        
        MAP[x1][y1 + 1] = temp
        
        answer.append(small)
    
    return answer