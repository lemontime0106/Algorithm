N = int(input())
sign = list(input().split())

visited = [False] * 10
answer = []

def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j

def solution(cnt, s):
    if cnt == N+1:
        answer.append(s)
        return

    for i in range(10):
        if visited[i]:
            continue

        if cnt == 0 or check(s[cnt-1], str(i), sign[cnt-1]):
            visited[i] = True
            solution(cnt + 1, s + str(i))
            visited[i] = False

solution(0, "")
answer.sort()
print(answer[-1])
print(answer[0])