def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    
    for i in range(n):
        arr1_bin.append(bin(arr1[i])[2:].zfill(n))
        arr2_bin.append(bin(arr2[i])[2:].zfill(n))
        
        temp = ""
        for j in range(n):
            if arr1_bin[i][j] == "1" or arr2_bin[i][j] == "1":
                temp += "#"
            elif arr1_bin[i][j] == "0" and arr2_bin[i][j] == "0":
                temp += " "
        answer.append(temp)
    
    return answer