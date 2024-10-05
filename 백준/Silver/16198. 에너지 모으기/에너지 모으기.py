N = int(input())
lst = list(map(int, input().split()))

answer = 0

def backtracking(x):
    global answer

    if len(lst) == 2:
        answer = max(answer, x)
        return

    for i in range(1, len(lst) - 1):
        target = lst[i-1] * lst[i+1]

        a = lst.pop(i)
        backtracking(x + target)
        lst.insert(i, a)

backtracking(0)
print(answer)