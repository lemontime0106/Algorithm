N = int(input())
stack = []
answer = []
flag = True

cur = 1
for _ in range(N):
    i = int(input())
    while cur <= i:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == i:
        stack.pop()
        answer.append("-")
    else:
        flag = False
        break

if flag:
    for i in answer:
        print(i)
else:
    print("NO")