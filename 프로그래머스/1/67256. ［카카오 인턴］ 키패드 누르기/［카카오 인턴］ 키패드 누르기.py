def solution(numbers, hand):
    answer = ''
    
    pad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    L = pad["*"]
    R = pad["#"]
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            L = pad[n]
        elif n in [3, 6, 9]:
            answer += "R"
            R = pad[n]
        else:
            left_dist = abs(L[0]-pad[n][0]) + abs(L[1]-pad[n][1])
            right_dist = abs(R[0]-pad[n][0]) + abs(R[1]-pad[n][1])
            
            if left_dist > right_dist:
                answer += "R"
                R = pad[n]
            elif left_dist < right_dist:
                answer += "L"
                L = pad[n]
            else:
                if hand == "left":
                    answer += "L"
                    L = pad[n]
                else:
                    answer += "R"
                    R = pad[n]
    
    return answer