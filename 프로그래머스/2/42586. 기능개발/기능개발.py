def solution(progresses, speeds):
    answer = []
    
    while progresses:
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        if count > 0:
            answer.append(count)
    
    return answer