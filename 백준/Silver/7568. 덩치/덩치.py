N = int(input())
lst = []

for _ in range(N):
    w, h = map(int, input().split())
    lst.append((w, h))

for i in lst:
    temp = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            temp += 1
    print(temp, end=" ")