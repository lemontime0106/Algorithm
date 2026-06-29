def solution(players, callings): 
    temp = dict()
    
    for i in range(len(players)):
        temp[players[i]] = i
    
    for call in callings:
        rank = temp[call]
        front = players[rank-1]
        
        players[rank-1], players[rank] = players[rank], players[rank-1]
        
        temp[call] -= 1
        temp[front] += 1
    
    return players