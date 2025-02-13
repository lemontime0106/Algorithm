N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = set()

def backtracking(cnt, stack):
    if len(stack) == M:
        answer.add(tuple(stack))
        return

    for i in range(cnt, N):
        stack.append(lst[i])
        backtracking(i + 1, stack)
        stack.pop()

backtracking(0, [])
for ans in sorted(answer):
    print(*ans)