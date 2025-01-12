N = int(input())

stack = []

for _ in range(N):
    i = int(input())

    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))