from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    
    for i in range(300000):
        if s1 > s2:
            s1 -= q1[0]
            s2 += q1[0]
            q2.append(q1.popleft())
        elif s1 < s2:
            s1 += q2[0]
            s2 -= q2[0]
            q1.append(q2.popleft())
        else:
            return i
    
    return -1