N = int(input())

lst = []

for _ in range(N):
    lst.append(int(input()))

cnt = 0

for i in range(N-1, 0, -1):
    if lst[i-1] >= lst[i]:
        cnt += (lst[i-1] - lst[i] + 1)
        lst[i-1] = lst[i] - 1

print(cnt)