from collections import deque

def bfs():
    q = deque()
    q.append([home[0], home[1]])

    while q:
        x, y = q.popleft()
        if abs(x - goal[0]) + abs(y - goal[1]) <= 1000:
            print("happy")
            return

        for i in range(N):
            if not visited[i]:
                nx, ny = conv[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = True

    print("sad")
    return

T = int(input())
for _ in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    conv = []
    for j in range(N):
        conv.append(list(map(int, input().split())))
    goal = list(map(int, input().split()))

    visited = [False] * (N+1)
    bfs()
