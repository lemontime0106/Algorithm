from collections import deque

N = int(input())
lst = list(map(int, input().split()))
S = int(input())

answer = 0
direct = [-1, 1]
visited = [False] * N

def bfs(start):
    q = deque()
    q.append(start)
    visited[start-1] = True

    while q:
        now = q.popleft()

        for d in direct:
            nx = now + (d * lst[now-1])

            if 0 < nx <= N and not visited[nx-1]:
                visited[nx - 1] = True
                q.append(nx)

bfs(S)

for i in range(N):
    if visited[i]:
        answer += 1

print(answer)