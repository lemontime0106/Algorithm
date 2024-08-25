def solution(arr):
    answer = 0
    n = 1
    while True:
        answer = max(arr) * n
        result = True
        for i in arr:
            if answer % i != 0:
                result = False
                break
        if result:
            break
        n += 1
    return answer