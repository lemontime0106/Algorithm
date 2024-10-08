N, K = map(int, input().split())
lst = list(map(int, input().split()))

answer = float("inf")
start, end = 0, 0

lion_count = 0

while end < N:
    if lst[end] == 1:
        lion_count += 1
    end += 1

    while lion_count >= K:
        answer = min(answer, end - start)

        if lst[start] == 1:
            lion_count -= 1
        start += 1

if answer == float("inf"):
    print(-1)
else:
    print(answer)
