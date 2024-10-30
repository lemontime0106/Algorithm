def solution(arr):
    answer = []
    
    cur = arr[0]
    for i in range(len(arr)):
        if cur != arr[i]:
            answer.append(cur)
            cur = arr[i]
        
        if i == len(arr) - 1:
            answer.append(arr[i])
    
    return answer