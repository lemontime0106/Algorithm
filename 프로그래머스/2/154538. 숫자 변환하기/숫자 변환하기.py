from collections import deque

def solution(x, y, n):
    q = deque([(x, 0)])
    visited = [False] * (y + 1)
    visited[x] = True

    while q:
        current, count = q.popleft()
        
        if current == y:
            return count
        
        for next_value in (current + n, current * 2, current * 3):
            if next_value <= y and not visited[next_value]:
                visited[next_value] = True
                q.append((next_value, count + 1))
    
    return -1