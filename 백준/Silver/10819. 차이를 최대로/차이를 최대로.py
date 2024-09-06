from itertools import permutations

N = int(input())
lst = list(map(int, input().split()))

answer = 0
for perm in permutations(lst):
    cur = 0
    for i in range(N - 1):
        cur += abs(perm[i] - perm[i + 1])
    answer = max(answer, cur)

print(answer)
