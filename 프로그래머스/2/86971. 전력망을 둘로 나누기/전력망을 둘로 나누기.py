from collections import deque

def solution(n, wires):
    answer = float("inf")

    for i in range(len(wires)):
        MAP = [[] for _ in range(n + 1)]

        for j in range(len(wires)):
            if i == j:
                continue

            a, b = wires[j]
            MAP[a].append(b)
            MAP[b].append(a)

        def bfs(start):
            q = deque([start])

            visited = [False] * (n + 1)
            visited[start] = True

            cnt = 1

            while q:
                v = q.popleft()

                for next_node in MAP[v]:
                    if not visited[next_node]:
                        visited[next_node] = True
                        q.append(next_node)
                        cnt += 1

            return cnt

        group1 = bfs(1)

        group2 = n - group1

        answer = min(answer, abs(group1 - group2))

    return answer