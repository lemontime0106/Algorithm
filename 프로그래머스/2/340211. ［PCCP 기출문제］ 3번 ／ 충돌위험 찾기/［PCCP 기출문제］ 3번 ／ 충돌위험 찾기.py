from collections import Counter

def solution(points, routes):
    def bfs(route):
        time = 0
        lst = []
        
        for i in range(len(route) - 1):
            sx, sy = points[route[i] - 1]
            ex, ey = points[route[i+1] - 1]
            
            while sx != ex:
                lst.append((sx, sy, time))
                if sx < ex:
                    sx += 1
                else:
                    sx -= 1
                time += 1
            
            while sy != ey:
                lst.append((sx, sy, time))
                if sy < ey:
                    sy += 1
                else:
                    sy -= 1
                time += 1
        lst.append((sx, sy, time))
        return lst
    
    second = []
    
    for route in routes:
        second.extend(bfs(route))
    res = 0
    temp = Counter(second)
    for i in temp.values():
        if i >= 2:
            res += 1
    
    return res