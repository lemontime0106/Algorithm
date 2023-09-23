N, L, R, X = map(int, input().split())
problem = list(map(int, input().split()))
comb = []
s = 0
for i in range(1 << N):
    temp = []
    for j in range(N):
        if i & (1 << j):
            temp.append(problem[j])
    if len(temp) < 2:
        continue

    if L <= sum(temp) <= R and max(temp) - min(temp) >= X:
        comb.append(temp)
print(len(comb))

