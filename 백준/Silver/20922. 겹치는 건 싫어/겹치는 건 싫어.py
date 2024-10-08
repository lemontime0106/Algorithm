from collections import defaultdict

N, K = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, 0
answer = 0

number = defaultdict(int)

while end < N:
    if number[lst[end]] >= K:
        number[lst[start]] -= 1
        start += 1
    else:
        number[lst[end]] += 1
        end += 1
        answer = max(answer, end - start)

print(answer)
