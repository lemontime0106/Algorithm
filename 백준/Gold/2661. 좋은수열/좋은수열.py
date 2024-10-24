N = int(input())
answer = []

def check(answer, cnt):
    for i in range(1, cnt // 2 + 1):
        if answer[-i:] == answer[-2*i:-i]:
            return False
    return True

def backtracking(cnt):
    if cnt == N:
        print("".join(map(str, answer)))
        exit(0)

    for i in range(1, 4):
        answer.append(i)
        if check(answer, cnt + 1):
            backtracking(cnt + 1)
        answer.pop()

backtracking(0)