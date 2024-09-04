from collections import Counter

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

answer = 0
c = Counter()

for i in range(N):
    for j in range(i, N):
        c[sum(A[i:j+1])] += 1

for i in range(M):
    for j in range(i, M):
        t = T - sum(B[i:j+1])
        answer += c[t]

print(answer)