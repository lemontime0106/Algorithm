import bisect

N = int(input())

B = [int(input()) for _ in range(N)]

all = set(range(1, 2*N+1))

A = sorted(list(all - set(B)))

A.sort()
score = 0

for b in B:
    idx = bisect.bisect_right(A, b)

    if idx < len(A):
        score += 1
        A.pop(idx)
    else:
        A.pop(0)

print(score)