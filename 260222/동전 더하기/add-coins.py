N, K = map(int, input().split())

token = [int(input().strip()) for _ in range(N)]

token.sort(reverse=True)

answer = 0

for coin in token:
    if K == 0:
        break

    cnt = K // coin
    answer += cnt
    K %= coin

print(answer)
