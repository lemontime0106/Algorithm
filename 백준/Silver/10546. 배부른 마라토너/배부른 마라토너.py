N = int(input())

dic = {}

for i in range(N):
    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

for _ in range(N-1):
    name = input()
    dic[name] -= 1

for i in dic:
    if dic[i]:
        print(i)
        break