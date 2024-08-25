def solution(s):
    answer = 0
    s = list(s)
    N = len(s)
    for _ in range(N):
        stack = []
        for i in range(N):
            if len(stack) > 0:
                if stack[-1] == '[' and s[i] == ']': 
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}': 
                    stack.pop()
                elif stack[-1] == '(' and s[i] == ')': 
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if len(stack) == 0:
            answer += 1
            
        s.append(s.pop(0))

        
    return answer