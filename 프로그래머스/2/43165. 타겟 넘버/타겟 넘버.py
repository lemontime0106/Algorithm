def solution(numbers, target):
    answer = [0]  

    def dfs(cur, idx):
        if len(numbers) == idx:
            if target == cur:
                answer[0] += 1  
            return
        
        dfs(cur + numbers[idx], idx + 1)
        dfs(cur - numbers[idx], idx + 1)

    dfs(0, 0)
    
    return answer[0]
