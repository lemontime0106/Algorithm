def find(parents, x):
    if parents[x] == x:
        return x
    
    return find(parents, parents[x])

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, costs):
    answer = 0
    
    parents = [i for i in range(n)]
    
    graph = []
    
    for a, b, c in costs:
        graph.append((c, a, b))
    
    graph.sort()
    
    for cost, a, b in graph:
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            answer += cost
    
    return answer