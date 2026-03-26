N = int(input())

start = 1
end = 1

curr = 1
cnt = 1

while end != N:
    if curr == N:
        cnt += 1
        end += 1
        curr += end

    elif curr < N:
        end += 1
        curr += end

    else:
        curr -= start
        start += 1


print(cnt)
