N = int(input())
permutation = []

def dfs():
    if len(permutation) == N:
        print(*permutation)
        return

    for i in range(1, N+1):
        if i not in permutation:
            permutation.append(i)
            dfs()
            permutation.pop()

dfs()