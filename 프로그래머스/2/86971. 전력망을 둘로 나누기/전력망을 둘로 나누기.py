def solution(n, wires):
    answer = float("inf")
    
    def bfs(start):
        q = []
        q.append(start)
        visited = [False] * (n + 1)
        visited[start] = True
        cnt = 1
        while q:
            v = q.pop(0)
            for k in graph[v]:
                if not visited[k]:
                    visited[k] = True
                    q.append(k)
                    cnt += 1
        return cnt
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue
            
            a, b = wires[j][0], wires[j][1]
            graph[a].append(b)
            graph[b].append(a)
        
        group1 = bfs(1)
        group2 = n - group1
        answer = min(answer, abs(n - (group1 * 2)))
        
    
    return answer