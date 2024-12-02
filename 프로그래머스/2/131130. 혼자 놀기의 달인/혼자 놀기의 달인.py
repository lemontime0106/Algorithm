def solution(cards):
    answer = []
    N = len(cards)
    visited = [False] * N
    
    for i in range(N):
        cnt = 0
        while not visited[i]:
            visited[i] = True
            i = cards[i] - 1
            cnt += 1
        answer.append(cnt)
    
    answer.sort(reverse=True)
            
    return answer[0] * answer[1]