answer = []
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    a = set([int(input()) for _ in range(N)])
    b = set([int(input()) for _ in range(M)])

    answer.append(len(a&b))

print(*answer)