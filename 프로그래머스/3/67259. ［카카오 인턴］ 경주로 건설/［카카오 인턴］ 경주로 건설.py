from collections import deque

def solution(board):
    direct = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    N = len(board)
    
    def bfs(x, y, cost, dir):
        visited = [[float("inf")] * N for _ in range(N)]
        visited[x][y] = cost
        
        q = deque([(x, y, cost, dir)])
        while q:
            x, y, cost, dir = q.popleft()
            for i in range(4):
                nx, ny = x + direct[i][0], y + direct[i][1]
                
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                    if i == dir:
                        ncost = cost + 100
                    else:
                        ncost = cost + 600
                    
                    if ncost < visited[nx][ny]:
                        visited[nx][ny] = ncost
                        q.append((nx, ny, ncost, i))
        
        return visited[N-1][N-1]
    
    answer = min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 2))
    
    return answer
