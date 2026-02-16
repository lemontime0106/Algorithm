N, M, K = map(int, input().split())
lst = list(map(int, input().split()))

position = [1] * K
answer = 0

def dfs(turn, score):
    global answer

    if turn == N:
        answer = max(answer, score)
        return

    for i in range(K):
        before = position[i]
        temp = 0

        if position[i] < M:
            position[i] += lst[turn]

            if position[i] >= M:
                position[i] = M
                temp = 1
        
        dfs(turn + 1, score+temp)
    
        position[i] = before
    
dfs(0, 0)

print(answer)
    
