w, h = map(int, input().split())
n = int(input())
dist = []
ans = 0
for _ in range(n+1):
    a, b = map(int, input().split())
    if a == 1:
        dist.append(2*w + h - b)
    elif a == 2:
        dist.append(b)
    elif a == 3:
        dist.append(2*w + h + b)
    elif a == 4:
        dist.append(w + h - b)

cur = dist.pop()

for i in range(n):
    ans += min(abs(dist[i] - cur), (2 * (w + h)) - abs(dist[i] - cur))

print(ans)
