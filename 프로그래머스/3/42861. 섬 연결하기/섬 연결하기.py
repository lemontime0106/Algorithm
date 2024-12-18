def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    global parent
    
    answer = 0
    parent = [i for i in range(n)]
    
    edges = []
    for a, b, c in costs:
        edges.append((c, a, b))
    
    edges.sort()
    
    for c, a, b in edges:
        if find_parent(a) != find_parent(b):
            union(a, b)
            answer += c
    
    return answer