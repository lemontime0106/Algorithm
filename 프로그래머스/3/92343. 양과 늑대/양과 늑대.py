def solution(info, edges):
    answer = []
    visited = [False] * len(info)
    
    def dfs(s, w):
        if s > w:
            answer.append(s)
        else:
            return
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(s + 1, w)
                else:
                    dfs(s, w + 1)
                visited[c] = 0
    visited[0] = 1
    dfs(1, 0)
    
    return max(answer)