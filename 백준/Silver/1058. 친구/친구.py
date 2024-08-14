N = int(input())

MAP = [list(input()) for _ in range(N)]

graph = [[0] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if MAP[i][j] == "Y" or (MAP[i][k] == "Y" and MAP[k][j] == "Y"):
                graph[i][j] = 1

answer = 0
for row in graph:
    answer = max(answer, sum(row))
print(answer)