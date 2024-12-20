N = int(input())
lst = []
acc = [0] * (N+1)

for i in range(N):
    lst.append(int(input()))
    acc[i+1] = acc[i] + lst[i]

total = acc[N]

answer = 0

for i in range(1, N+1):
    start, end = i, N

    while start <= end:
        mid = (start + end) // 2
        l1 = acc[mid] - acc[i-1]
        l2 = total - l1

        if l1 < l2:
            start = mid + 1
        else:
            end = mid - 1

        answer = max(answer, min(l1, l2))

print(answer)