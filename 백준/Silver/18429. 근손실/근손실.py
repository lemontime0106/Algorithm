N, K = map(int, input().split())
kit = list(map(int, input().split()))
answer = 0
visited = [False] * N

def backtracking(w, k):
    global answer

    if w < 0:
        return

    if k >= N:
        answer += 1
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtracking(w + kit[i] - K, k+1)
            visited[i] = False

backtracking(0, 0)

print(answer)