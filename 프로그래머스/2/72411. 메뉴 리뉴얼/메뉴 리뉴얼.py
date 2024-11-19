from collections import defaultdict

def solution(orders, course):
    answer = []
    
    food = defaultdict(int)
    
    def dfs(start, stack, cnt, order):
        if len(stack) == cnt:
            f = "".join(sorted(stack))
            food[f] += 1
            return
        
        for i in range(start, len(order)):
            stack.append(order[i])
            dfs(i+1, stack, cnt, order)
            stack.pop()
    
    for order in orders:
        for cnt in course:
            dfs(0, [], cnt, sorted(order))
    
    
    for cnt in course:
        max_cnt = 2
        temp = []
        
        for f, count in food.items():
            if len(f) == cnt:
                if count > max_cnt:
                    temp = [f]
                    max_cnt = count
                elif count == max_cnt:
                    temp.append(f)
        answer.extend(temp)
    
    return sorted(answer)