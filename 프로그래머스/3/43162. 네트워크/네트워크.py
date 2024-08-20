def solution(n, computers):
    cnt = 0
    
    graph = [[] for _ in range(n) ]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]:
                graph[i].append(j)
    
    visited = [False] * (n + 1)
    
    def bfs(x):
        q = []
        q.append(x)
        visited[x] = True
        
        while q:
            v = q.pop(0)
            for j in graph[v]:
                if not visited[j]:
                    visited[j] = True
                    q.append(j)
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
    
    for i in visited:
        if not i:
            cnt += 1
    
    return cnt - 1