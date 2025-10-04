from collections import deque

def solution(maps):
    answer = 0
    
    N = len(maps)
    M = len(maps[0])
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = deque([(0, 0)])
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                    
    if maps[N-1][M-1] == 1:
        return -1
    
    elif maps[N-1][M-1] != 1:
        return maps[N-1][M-1]