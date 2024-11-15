from collections import deque

def solution(places):
    answer = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    q = deque([(i, j)])
                    visited = [[False] * 5 for _ in range(5)]
                    visited[i][j] = True
                    distance = [[0] * 5 for _ in range(5)]
                    
                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            
                            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                                if place[nx][ny] == "X":
                                    continue
                                
                                if place[nx][ny] == "P":
                                    if distance[x][y] + 1 <= 2:
                                        return 0
                                
                                if place[nx][ny] == "O":
                                    q.append((nx, ny))
                                    visited[nx][ny] = True
                                    distance[nx][ny] = distance[x][y] + 1

        return 1
    
    for place in places:
        answer.append(bfs(place))
        
    return answer
