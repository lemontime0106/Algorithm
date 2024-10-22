N, H = map(int, input().split())

up = [0] * (H+1)
down = [0] * (H+1)

answer = [N, 0]

for i in range(N):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(H-1, 0, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

for i in range(1, H+1):
    temp = up[H-i+1] + down[i]
    if answer[0] == temp:
        answer[1] += 1
        continue

    if answer[0] > temp:
        answer[0] = temp
        answer[1] = 1

print(*answer)