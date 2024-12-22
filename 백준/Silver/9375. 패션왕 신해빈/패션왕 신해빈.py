from collections import defaultdict

for _ in range(int(input())):
    wear = defaultdict(list)
    N = int(input())
    for _ in range(N):
        name, type = input().split()
        wear[type].append(name)

    cnt = 1

    for i in wear:
        cnt *= (len(wear[i]) + 1)

    print(cnt-1)