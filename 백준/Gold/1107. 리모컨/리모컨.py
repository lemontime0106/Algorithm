N = int(input())
M = int(input())

if M == 0:
    broken = []
else:
    broken = list(map(int, input().split()))

answer = abs(100 - N)

for i in range(999999):
    num = str(i)

    for j in num:
        if int(j) in broken:
            break

    else:
        answer = min(answer, abs(N - i) + len(num))

print(answer)