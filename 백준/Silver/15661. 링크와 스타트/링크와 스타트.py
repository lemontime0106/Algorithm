N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

lst = set(list(range(N)))
ans = float('inf')
arr_1 = []
arr_2 = []
for i in range(1 << N):
    temp = set()
    for j in range(N):
        if i & (1 << j):
            temp.add(j)
    comb = lst - temp
    if len(comb) == N or len(comb) == 0:
        continue
    arr_1.append(list(comb))
    arr_2.append(list(temp))
# print(arr_1, arr_2)
group1, group2 = [], []
for a1 in arr_1:
    power_1 = 0
    for i in range(len(a1)):
        for j in range(i+1, len(a1)):
            power_1 += MAP[a1[i]][a1[j]]
            power_1 += MAP[a1[j]][a1[i]]
    group1.append(power_1)
for a2 in arr_2:
    power_2 = 0
    for i in range(len(a2)):
        for j in range(i+1, len(a2)):
            power_2 += MAP[a2[i]][a2[j]]
            power_2 += MAP[a2[j]][a2[i]]
    group2.append(power_2)

for i in range(len(group1)):
    ans = min(ans, abs(group1[i] - group2[i]))

print(ans)


