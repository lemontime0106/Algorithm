N, X = map(int, input().split())
lst = list(map(int, input().split()))

if max(lst) != 0:
    cur = sum(lst[:X])
    max_cur = cur
    cnt = 1

    for i in range(X, N):
        cur += lst[i]
        cur -= lst[i-X]

        if cur > max_cur:
            max_cur = cur
            cnt = 1
        elif cur == max_cur:
            cnt += 1

    print(max_cur)
    print(cnt)

else:
    print("SAD")