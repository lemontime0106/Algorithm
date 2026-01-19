T = int(input())

for i in range(T):
    N = int(input())
    words = input().strip()

    stack = []

    for word in words:
        stack.append(word)

        if (len(stack)) >= 3 and stack[-3:] == ["f", "o", "x"]:
            stack.pop()
            stack.pop()
            stack.pop()

    print(len(stack))