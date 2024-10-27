N, K = map(int, input().split())
lst = list(map(int, input().split()))

answer = []

for i in range(1, N):
    answer.append(lst[i] - lst[i-1])

answer.sort(reverse=True)
print(sum(answer[K-1:]))