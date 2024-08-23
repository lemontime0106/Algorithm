def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                answer = False
                break
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    answer = False
                    break
    
    if len(stack) > 0:
        answer = False
    
    return answer