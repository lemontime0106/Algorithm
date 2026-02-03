N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
answer = -1

for x1 in range(N):
    for y1 in range(M):
        for x2 in range(x1, N):
            for y2 in range(y1, M):
                flag = True

                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        if MAP[i][j] <= 0:
                            flag = False
                            break
                    
                    if not flag:
                        break
                
                if flag:
                    area = (x2 - x1 + 1) * (y2 - y1 + 1)
                    answer = max(answer, area)

print(answer)