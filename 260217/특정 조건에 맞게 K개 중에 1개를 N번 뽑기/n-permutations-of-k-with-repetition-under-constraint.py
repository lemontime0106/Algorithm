K, N = map(int, input().split())

lst = []

def dfs():
    if len(lst) == N:
        print(*lst)
        return
    
    for i in range(1, K+1):
        if len(lst) >= 2 and lst[-1] == lst[-2] == i:
            continue
        
        lst.append(i)
        dfs()
        lst.pop()

dfs()