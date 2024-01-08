N, L = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

start = lst[0]
cnt = 1

for i in lst[1:]:
    if (i + 0.5) - (start - 0.5) <= L:
        continue
    else:
        start = i
        cnt += 1
print(cnt)
