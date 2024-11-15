N = int(input())

answer = 1

for _ in range(N):
    answer *= N
    N -= 1

print(answer)