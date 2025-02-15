N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]

answer = []
idx = 0

for i in range(N):
    idx += K - 1
    if idx >= len(lst):
        idx = idx % len(lst)

    answer.append(str(lst.pop(idx)))

print("<", ", ".join(answer[:]), ">", sep="")