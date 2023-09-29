import heapq
cup = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    cup.append((a, b))
cup.sort(key=lambda x: (x[0], x[1]))
ans = []
for i in cup:
    heapq.heappush(ans, i[1])
    if i[0] < len(ans):
        heapq.heappop(ans)

print(sum(ans))
