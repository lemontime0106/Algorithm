N = int(input())

lst = list(map(int, input().split()))

cur = lst[0]
answer = lst[0]

for i in range(1, N):
    cur = max(lst[i], cur + lst[i])
    answer = max(answer, cur)

print(answer)