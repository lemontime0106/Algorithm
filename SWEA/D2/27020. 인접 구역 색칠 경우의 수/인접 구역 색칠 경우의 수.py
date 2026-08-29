# 27020. 인접 구역 색칠 경우의 수

def dfs(idx):
    global answer

    if idx == N:
        answer += 1
        return

    for color in range(K):
        possible = True

        for next_node in MAP[idx]:

            if colors[next_node] == -1:
                continue

            if colors[next_node] == color:
                possible = False
                break

        if possible:
            colors[idx] = color
            dfs(idx+1)
            colors[idx] = -1


for t in range(1, int(input())+1):
    N, M, K = map(int, input().split())

    MAP = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())

        a -= 1
        b -= 1

        MAP[a].append(b)
        MAP[b].append(a)

    colors = [-1] * N
    answer = 0

    dfs(0)

    print(f"#{t} {answer}")