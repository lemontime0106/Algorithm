N, K = map(int, input().split())
ans = 0
while True:
    if bin(N).count('1') <= K:
        break
    N += 1
    ans += 1
print(ans)