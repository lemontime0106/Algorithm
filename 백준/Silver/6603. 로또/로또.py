while True:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break

    else:
        N = lst[0]
        lst = lst[1:]

        visited = [False] * N
        answer = []

        def dfs(start, stack):
            if len(stack) == 6:
                answer.append(stack[:])
                return

            for i in range(start, N):
                if not visited[i]:
                    visited[i] = True
                    stack.append(lst[i])
                    dfs(i+1, stack)
                    stack.pop()
                    visited[i] = False

        dfs(0, [])
        for i in answer:
            print(*i)
        print()