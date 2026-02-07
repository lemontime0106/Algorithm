N = int(input())

answer = 0

def dfs(cnt):
    global answer

    if cnt == N:
        answer += 1
        return
    
    if cnt > N:
        return

    for i in range(1, 5):
        dfs(cnt + i)

dfs(0)
print(answer)