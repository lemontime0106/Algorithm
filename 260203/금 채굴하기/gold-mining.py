N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def cost(K):
    return K ** 2 + (K+1) ** 2

answer = 0

for i in range(N):
    for j in range(N):
        gold = 0

        for k in range(0, 2*N):
            gold = 0

            for x in range(N):
                for y in range(N):
                    if abs(x - i) + abs(y - j) <= k:
                        if MAP[x][y] == 1:
                            gold += 1
            
            if gold * M >= cost(k):
                answer = max(answer, gold)

print(answer)