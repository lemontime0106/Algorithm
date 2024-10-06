from collections import defaultdict, deque

N = int(input())
option = defaultdict(list)

for _ in range(N):
    a, b = map(str, input().split(" is "))
    option[a].append(b)

M = int(input())

def bfs(s, e):
    q = deque([s])
    visited = set()

    while q:
        v = q.popleft()
        if v == e:
            return True
        visited.add(v)
        for i in option[v]:
            if i not in visited:
                q.append(i)
    return False

for _ in range(M):
    a, b = map(str, input().split(" is "))
    if bfs(a, b):
        print("T")
    else:
        print("F")
