# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금

def dfs(cnt):
    global answer

    if cnt == N:
        answer = max(answer, int("".join(nums)))
        return

    current = "".join(nums)

    if current in visited[cnt]:
        return

    visited[cnt].add(current)

    for i in range(L-1):
        for j in range(i+1, L):
            nums[i], nums[j] = nums[j], nums[i]

            dfs(cnt+1)

            nums[i], nums[j] = nums[j], nums[i]

for t in range(1, int(input())+1):
    num, N = input().split()

    nums = list(num)
    N = int(N)

    L = len(nums)

    visited = [set() for _ in range(N+1)]
    answer = 0

    dfs(0)

    print(f"#{t} {answer}")
