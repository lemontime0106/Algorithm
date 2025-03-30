N, M = map(int, input().split())
answer = 0

S = set()
for i in range(N):
    S.add(input())
    

for _ in range(M):
    t = input()
    if t in S:
        answer+=1
        
print(answer)