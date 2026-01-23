N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
answer= float("inf")

def dfs(idx, cnt):
    global answer

    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    start += MAP[i][j] + MAP[j][i]

                elif not visited[i] and not visited[j]:
                    link += MAP[i][j] + MAP[j][i]

        answer = min(answer, abs(start - link))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False


visited[0] = True
dfs(1, 1)

print(answer)