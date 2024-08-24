def solution(k, dungeons):
    def dfs(current_k, cnt, visited):
        max_count = cnt
        
        for i in range(len(dungeons)):
            if not visited[i] and current_k >= dungeons[i][0]:
                visited[i] = True
                max_count = max(max_count, dfs(current_k - dungeons[i][1], cnt + 1, visited))
                visited[i] = False
        
        return max_count
    
    visited = [False] * len(dungeons)
    answer = dfs(k, 0, visited)
    
    return answer