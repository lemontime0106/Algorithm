def solution(edges):
    # 생성된 노드 : 들어오는거 X, 나가는거 2개 이상
    # 도넛 : in, out : 1, 1
    # 막대 : in, out : 0, 1
    # 8자 : in, out : 2, 2
    
    n = len(edges) + 1
    answer = [[0, 0] for _ in range(n + 1)]
    sol = [0, 0, 0, 0]
    
    for edge in edges:
        a, b = edge[0], edge[1]
        answer[a][0] += 1
        answer[b][1] += 1
    
    for i in range(1, n + 1):
        in_out = answer[i]
        if in_out[0] >= 2 and in_out[1] == 0:
            sol[0] = i
        elif in_out[0] == 0 and in_out[1] > 0:
            sol[2] += 1
        elif in_out[0] >= 2 and in_out[1] >= 2:
            sol[3] += 1
    
    sol[1] = answer[sol[0]][0] - sol[2] - sol[3]
    
    return sol
