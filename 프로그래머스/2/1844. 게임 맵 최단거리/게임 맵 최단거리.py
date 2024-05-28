from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    q = deque()
    q.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        x, y = q.popleft()
        for d in direct:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    if visited[N-1][M-1] == 0:
        answer = -1
    else:
        answer = visited[N-1][M-1]
    
    return answer