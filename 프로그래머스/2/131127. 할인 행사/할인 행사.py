def solution(want, number, discount):
    answer = 0
    N = len(want)
    want_dict = {}
    for i in range(N):
        want_dict[want[i]] = number[i]
    
    M = len(discount)
    days = sum(number)
    
    for i in range(M-days+1):
        cart = {}
        for j in range(days):
            temp = discount[i:days+i]
            if temp[j] not in cart:
                cart[temp[j]] = 1
            else:
                cart[temp[j]] += 1
        
        if cart == want_dict:
            answer += 1

    return answer