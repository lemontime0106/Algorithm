N, K = map(int, input().split())
lst = list(map(int, input().split()))
answer = []

def solution(l):
    if len(l) == 1:
        return l

    mid = (len(l) + 1) // 2

    left = solution(l[:mid])
    right = solution(l[mid:])

    i, j = 0, 0
    l2 = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l2.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            l2.append(right[j])
            answer.append(right[j])
            j += 1

    while i < len(left):
        l2.append(left[i])
        answer.append(left[i])
        i += 1

    while j < len(right):
        l2.append(right[j])
        answer.append(right[j])
        j += 1

    return l2

solution(lst)

if len(answer) >= K:
    print(answer[K-1])
else:
    print(-1)