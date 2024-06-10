def solution(N, road, K):
    answer = 0
    
    visited = [False] * (N + 1)
    distance = [float("inf")] * (N + 1)
    graph = [[] for _ in range(N+1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    def get_smallest_node():
        min_val = float("inf")
        index = 0
        for i in range(1, N+1):
            if distance[i] < min_val and not visited[i]:
                min_val = distance[i]
                index = i
        return index
    
    def dijkstra(start):
        distance[start] = 0
        for _ in range(N):
            now = get_smallest_node()
            if now == 0:  # 더 이상 방문할 수 있는 노드가 없을 경우
                break
            visited[now] = True
            for b, c in graph[now]:
                if not visited[b]:
                    distance[b] = min(distance[b], distance[now] + c)
    
    dijkstra(1)
        
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
              
    return answer