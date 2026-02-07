K, N = map(int, input().split())

answer = []

def dfs(cnt):
    if cnt == N:
        print(*answer)
        return

    for i in range(1, K+1):
        answer.append(i)
        dfs(cnt+1)
        answer.pop()

dfs(0)

