N = int(input())

cost = []

for _ in range(N):
    cost.append(list(map(int, input().split())))

cost.sort(key=lambda x: (x[0], x[1]))

total = [0] * N

for i in range(N):
    for j in range(i, N):
        temp = cost[i][0] - cost[j][1]
        if temp > 0:
            total[i] += temp

answer = [cost[i][0] for i in range(N) if total[i] == max(total)]

if sum(total) <= 0:
    print(0)
else:
    print(min(answer))