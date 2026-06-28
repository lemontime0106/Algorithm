def solution(arr1, arr2):    
    N = len(arr1)
    M = len(arr1[0])
    
    answer = [[] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            answer[i].append(arr1[i][j]+arr2[i][j])
    
    return answer