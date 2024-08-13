N, d, k, c = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

answer = 0

for i in range(N):
    temp = set()
    temp.add(c)
    for j in range(k):
        temp.add(lst[i-N+j])
    answer = max(answer, len(temp))

print(answer)