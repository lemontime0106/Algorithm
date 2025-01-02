N = int(input())
MAP = [input() for _ in range(N)]

heart = []
arm_left, arm_right, waist, leg_left, leg_right  = 0, 0, 0, 0, 0

for i in range(N):
    for j in range(N):
        if MAP[i][j] == "*":
            heart = [i+2, j+1]
            break
    if len(heart) > 0:
        break

for i in range(heart[1] - 1):
    if MAP[heart[0] - 1][i] == "*":
        arm_left += 1

for i in range(heart[1], N):
    if MAP[heart[0]-1][i] == "*":
        arm_right += 1

length = 0
for i in range(heart[0], N):
    if MAP[i][heart[1] - 1] == '*':
        waist += 1
        length = i

for i in range(N - 1, length, -1):
    if MAP[i][heart[1] - 2] == "*":
        leg_left += 1

for i in range(N - 1, length, -1):
    if MAP[i][heart[1]] == "*":
        leg_right += 1

print(*heart)
print(arm_left, arm_right, waist, leg_left, leg_right)