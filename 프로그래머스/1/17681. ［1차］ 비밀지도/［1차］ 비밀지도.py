def to_binary(num, n):
    if num == 0:
        return "0" * n
    
    result = ""
    
    while num > 0:
        result = str(num%2) + result
        num //= 2
    
    return result.zfill(n)
    

def solution(n, arr1, arr2):
    answer = []
    
    temp1 = []
    temp2 = []
    
    for i in range(n):
        temp1.append(to_binary(arr1[i], n))
        temp2.append(to_binary(arr2[i], n))
        
    for i in range(n):
        row = ""
        for j in range(n):
            if temp1[i][j] == "1" or temp2[i][j] == "1":
                row += "#"
            else:
                row += " "
        answer.append(row)
                
    return answer