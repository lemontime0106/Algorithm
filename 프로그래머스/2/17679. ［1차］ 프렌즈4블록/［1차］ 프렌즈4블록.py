def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    
    def check(x, y):
        cur = board[x][y]
        
        if cur != ' ' and board[x+1][y] == cur and board[x][y+1] == cur and board[x+1][y+1] == cur:
            return True
        return False
    
    
    
    def play():
        lst = set()
        for i in range(m-1):
            for j in range(n-1):
                if check(i, j):
                    lst.update([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
        return lst
    
    def drop():
        for j in range(n):
            row = m-1
            for i in range(m-1, -1, -1):
                if board[i][j] != " ":
                    board[row][j] = board[i][j]
                    if row != i:
                        board[i][j] = " "
                    row -= 1
    
    while True:
        remove_set = play()
        if not remove_set:
            break
            
        answer += len(remove_set)
        
        for x, y in remove_set:
            board[x][y] = " "
        
        drop()
    
    return answer