def solution(word):
    lst = ["A", "E", "I", "O", "U"]
    dic = []
    
    def dfs(cnt, s):
        if cnt == 5:
            return
        for i in range(len(lst)):
            dic.append(s + lst[i])
            dfs(cnt + 1, s + lst[i])
    dfs(0, "")
    
    return dic.index(word) + 1