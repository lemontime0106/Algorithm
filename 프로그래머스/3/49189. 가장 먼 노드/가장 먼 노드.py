from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    
    node = defaultdict(list)
    
    for i, j in edge:
        node[i].append(j)
        node[j].append(i)
        
    visited = [50001 for _ in range(n+1)]
    visited[0] = 0
    visited[1] = 0
    
    q = deque([[1, 1]])
    
    while q:
        p, cnt = q.popleft()
        
        for i in node[p]:
            if cnt < visited[i]:
                visited[i] = cnt
                q.append([i, cnt+1])
    
    visited.sort(reverse=True)
    
    M = visited[0]
    
    for i in visited:
        if i == M:
            answer += 1
        else:
            break
    
    return answer