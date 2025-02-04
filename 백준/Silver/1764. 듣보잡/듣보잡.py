N, M = map(int, input().split())
lst = dict()

for _ in range(N):
    a = input()

    if a not in lst:
        lst[a] = 1
    else:
        lst[a] += 1

for _ in range(M):
    a = input()

    if a not in lst:
        lst[a] = 1
    else:
        lst[a] += 1

answer = []

for i in lst.items():
    if i[1] == 2:
        answer.append(i[0])

answer.sort()

print(len(answer))
for i in answer:
    print(i)