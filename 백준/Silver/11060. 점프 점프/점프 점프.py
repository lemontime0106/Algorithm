from collections import deque

N = int(input())
lst = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    visited = [0] * (N+1)
    q = deque([1])

    while q:
        x = q.popleft()
        if x + lst[x-1] >= N:
            print(visited[x] + 1)
            break
        for i in range(1, lst[x-1]+1):
            nx = x + i
            if not visited[nx]:
                q.append(nx)
                visited[nx] = visited[x] + 1
    else:
        print(-1)