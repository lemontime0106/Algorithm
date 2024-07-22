N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            house.append((i, j))
        elif MAP[i][j] == 2:
            chicken.append((i, j))

comb = []


def dfs(start, stack):
    if len(stack) == M:
        comb.append(stack[:])
        return
    for k in range(start, len(chicken)):
        stack.append(chicken[k])
        dfs(k + 1, stack)
        stack.pop()


dfs(0, [])


def get_chicken_distance(chicken_combination):
    total_distance = 0
    for hx, hy in house:
        min_distance = float('inf')
        for cx, cy in chicken_combination:
            distance = abs(hx - cx) + abs(hy - cy)
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance
    return total_distance


min_distance = float('inf')
for c in comb:
    current_distance = get_chicken_distance(c)
    if current_distance < min_distance:
        min_distance = current_distance

print(min_distance)
