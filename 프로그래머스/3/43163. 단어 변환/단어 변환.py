from collections import deque

def bfs(b, t, w):
    q = deque()
    q.append([b, 0])
    
    while q:
        now, cnt = q.popleft()
        
        if now == t:
            return cnt
        
        for i in w:
            temp = 0
            for j in range(len(now)):
                if now[j] != i[j]:
                    temp += 1
            if temp == 1:
                q.append([i, cnt + 1])

def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)

        


        