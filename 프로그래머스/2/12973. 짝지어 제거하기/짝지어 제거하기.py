def solution(s):
    stack = []
    for a in s:
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)

    if len(stack) == 0:
        return 1
    else:
        return 0
