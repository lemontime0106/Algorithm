def solution(s):
    if len(s) == 1:
        return 1

    answer = []

    for i in range(1, len(s) // 2 + 1):
        compressed = "" 
        temp = s[:i]  
        count = 1  

        for j in range(i, len(s), i):
            if temp == s[j:j+i]: 
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + temp
                else:
                    compressed += temp
                temp = s[j:j+i]
                count = 1

        if count > 1:
            compressed += str(count) + temp
        else:
            compressed += temp

        answer.append(len(compressed))

    return min(answer)