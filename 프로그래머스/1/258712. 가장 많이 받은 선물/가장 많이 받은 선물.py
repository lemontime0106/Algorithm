def solution(friends, gifts):    
    result = [0] * len(friends)
    score = [0] * len(friends)
    lst = [{friend: 0 for friend in friends} for _ in range(len(friends))]
    
    for gift in gifts:
        a, b = gift.split()
        if a in friends and b in friends:
            score[friends.index(a)] += 1
            score[friends.index(b)] -= 1
            lst[friends.index(a)][b] += 1
    
    for i in range(len(friends)):
        curr = friends[i]
        for j in range(i + 1, len(friends)):
            friend = friends[j]
            a = lst[i][friend]
            b = lst[j][curr]
            if a > b:
                result[i] += 1
            elif a < b:
                result[j] += 1
            else:
                if score[i] > score[j]:
                    result[i] += 1
                elif score[i] < score[j]:
                    result[j] += 1
    
    answer = max(result)    
    
    return answer
