for _ in range(int(input())):
    word = sorted(list(input()))
    N = len(word)
    visited = [False] * N

    def dfs(stack, ):
        if len(stack) == N:
            print("".join(stack))
            return

        prev = ""
        for i in range(N):
            if not visited[i] and word[i] != prev:
                visited[i] = True
                stack.append(word[i])
                dfs(stack)
                stack.pop()
                visited[i] = False
                prev = word[i]

    dfs([])