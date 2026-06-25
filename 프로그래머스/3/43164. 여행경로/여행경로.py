def solution(tickets):
    graph = dict()
    
    for s, e in tickets:
        if s not in graph:
            graph[s] = [e]
        else:
            graph[s].append(e)
            
    for i in graph:
        graph[i].sort()
        
    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            return path
        
        if airport not in graph:
            return None
        
        for i in range(len(graph[airport])):
            next_airport = graph[airport].pop(i)
            
            result = dfs(next_airport, path+[next_airport])
            if result:
                return result
            
            graph[airport].insert(i, next_airport)
    
    return dfs("ICN", ["ICN"])