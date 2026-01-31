from collections import deque

T = int(input())

def bfs(N, MAP):
    color = [-1] * N

    for i in range(N):
        if color[i] != -1:
            continue

        q = deque([i])
        color[i] = 0

        while q:
            cur = q.popleft()
            for nxt in MAP[cur]:
                if color[nxt] == -1:
                    color[nxt] = 1 - color[cur]
                    q.append(nxt)
                elif color[nxt] == color[cur]:
                    return False
    return True

for _ in range(T):
    N, M = map(int, input().split())

    MAP = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        MAP[a].append(b)
        MAP[b].append(a)

    if bfs(N, MAP):
        print("possible")
    else:
        print("impossible")
