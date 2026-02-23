N, M = map(int, input().split())

lst = []

for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b, b / a))

lst.sort(key=lambda x: x[2], reverse=True)

remain = M
answer = 0.0

for w, v, ratio in lst:
    if remain == 0:
        break

    if remain >= w:
        answer += v
        remain -= w

    else:
        answer += ratio * remain
        remain = 0

print(f"{answer:.3f}")