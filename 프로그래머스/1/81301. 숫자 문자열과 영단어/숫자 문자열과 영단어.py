def solution(s):
    answer = ""
    
    s = list(s)
    
    number = {
        "one" : 1, "two" : 2, "three" : 3,
        "four" : 4, "five" : 5, "six" : 6,
        "seven" : 7, "eight" : 8, "nine" : 9, "zero" : 0
    }
    
    temp = ""
    
    while s:
        a = s.pop(0)
        
        if a.isdigit():
            answer += a
        else:
            temp += a
            if temp in number:
                answer += str(number[temp])
                temp = ""

    answer = int(answer)
    
    return answer