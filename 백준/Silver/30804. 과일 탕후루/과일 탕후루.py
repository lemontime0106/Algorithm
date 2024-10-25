from collections import defaultdict

N = int(input())
lst = list(map(int, input().split()))

left, right, cnt = 0, 0, 0
kind = defaultdict(int)
answer = 0

while right < N:
    if kind[lst[right]] == 0:
        cnt += 1
    kind[lst[right]] += 1

    while cnt > 2:
        kind[lst[left]] -= 1
        if kind[lst[left]] == 0:
            cnt -= 1
        left += 1

    answer = max(answer, right - left + 1)
    right += 1

print(answer)