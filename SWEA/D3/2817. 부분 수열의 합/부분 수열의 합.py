# 2817. 부분 수열의 합

for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    answer = 0

    def dfs(start, stack):
        global answer

        if sum(stack) == K:
            answer += 1
            return

        if sum(stack) > K:
            return

        for i in range(start, N):
            stack.append(lst[i])
            dfs(i+1, stack)
            stack.pop()

    dfs(0, [])

    print(f"#{t} {answer}")

