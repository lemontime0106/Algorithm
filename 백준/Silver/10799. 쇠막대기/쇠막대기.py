lst = list(input())

stack = []
answer = 0
for i in range(len(lst)):
    if lst[i] == "(":
        stack.append("(")
    else:
        if lst[i-1] == "(":
            stack.pop()
            answer += len(stack)

        else:
            stack.pop()
            answer += 1

print(answer)