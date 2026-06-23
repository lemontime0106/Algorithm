from collections import deque

def solution(maps):
    answer = 0
    
    N = len(maps)
    M = len(maps[0])
    
    visited = [[-1] * M for _ in range(N)]
    
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
        
    if visited[N-1][M-1] == -1:
        return -1

    return visited[N-1][M-1] + 1