N = int(input())
answer = 0

for _ in range(N):
    word = list(input())
    length = len(word)

    stack = []

    for i in word:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if not stack:
        answer += 1

print(answer)