N = int(input())
lst = list(map(int, input().split()))

balloon = []
for i in range(1, N+1):
    balloon.append((i, lst[i-1]))

answer = []
idx = 0
while balloon:
    temp = balloon.pop(idx)
    answer.append(temp[0])

    if not balloon:
        break

    if temp[1] < 0:
        idx = (idx + temp[1]) % len(balloon)
    else:
        idx = (idx + temp[1] - 1) % len(balloon)

print(*answer)