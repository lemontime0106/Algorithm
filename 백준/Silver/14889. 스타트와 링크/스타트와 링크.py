N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
answer = float("inf")

def dfs(a, b):
    global answer

    # 조기 종료 조건: 능력치 차이가 0이면 최적이므로 바로 종료
    if answer == 0:
        return

    if a == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += MAP[i][j]
                elif not visited[i] and not visited[j]:
                    link += MAP[i][j]
        answer = min(answer, abs(start - link))
        return

    for i in range(b, N):
        if not visited[i]:
            visited[i] = True
            dfs(a+1, i+1)  # 탐색 시작 지점을 i+1로 조정하여 중복 탐색 방지
            visited[i] = False

dfs(0, 0)
print(answer)