def solution(n):
    one = format(n, "b").count("1")
    
    for i in range(n+1, 1000001):
        if one == format(i, "b").count("1"):
            return i