import math

M = int(input())
N = int(input())

result = []

for i in range(int(math.sqrt(M)), int(math.sqrt(N)) + 1):
    square = i * i
    if M <= square <= N:
        result.append(square)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))