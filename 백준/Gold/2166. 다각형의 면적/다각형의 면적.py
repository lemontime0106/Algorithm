N = int(input())
point = []

for _ in range(N):
    point.append(list(map(int, input().split())))
point.append(point[0])

answer = 0
for i in range(N):
    answer += point[i][0] * point[i+1][1] - point[i+1][0] * point[i][1]

print(abs(answer) / 2)