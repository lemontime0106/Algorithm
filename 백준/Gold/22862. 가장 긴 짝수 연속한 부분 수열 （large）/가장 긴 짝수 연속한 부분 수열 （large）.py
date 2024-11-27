N, K = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0
start, end = 0, 0
odd = 0

while end < N:
    if odd > K:
        if lst[start] % 2 == 1:
            odd -= 1
        start += 1
        continue
    else:
        if lst[end] % 2 == 1:
            odd += 1
        end += 1

    answer = max(answer, (end - start - odd))
print(answer)