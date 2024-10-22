N = int(input())
lst = list(map(int, input().split()))

answer = 0
sum_lst = [lst[0]]

for i in range(1, N):
    sum_lst.append(sum_lst[i-1] + lst[i])

for i in range(1, N-1):
    right = 2 * sum_lst[-1] - (lst[0] + lst[i] + sum_lst[i])
    left = sum_lst[-1] - lst[i] - lst[-1] + sum_lst[i-1]
    mid = sum_lst[i] - lst[0] + sum_lst[-1] - sum_lst[i-1] - lst[-1]
    answer = max(answer, right, left, mid)

print(answer)