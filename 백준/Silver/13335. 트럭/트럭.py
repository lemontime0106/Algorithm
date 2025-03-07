N, W, L = map(int, input().split())
lst = list(map(int, input().split()))

q = [0] * W
answer = 0

while q:
    answer += 1
    q.pop(0)

    if lst:
        if sum(q) + lst[0] <= L:
            q.append(lst.pop(0))
        else:
            q.append(0)

print(answer)