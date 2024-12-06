N, M = map(int, input().split())

lst = list(map(int, input().split())) if M > 0 else []

answer = 0

def backtracking(stack):
    global answer
    if len(stack) == N:
        if not lst or all(num in stack for num in lst):
            answer += 1
        return

    for i in range(10):
        stack.append(i)
        backtracking(stack)
        stack.pop()

for i in range(10):
    backtracking([i])

print(answer)
