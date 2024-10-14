N, K = map(int, input().split())

burger = list(input())
answer = 0

for i in range(N):
    if burger[i] == "P":
        for j in range(i-K, i+K+1):
            if 0 <= j < N and burger[j] == "H":
                answer += 1
                burger[j] = "X"
                break

print(answer)