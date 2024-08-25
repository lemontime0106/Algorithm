def solution(want, number, discount):
    ans = 0
    N = len(want)
    want_dict = {}
    for i in range(N):
        want_dict[want[i]] = number[i]
    
    M = len(discount)
    days = sum(number)
    
    for i in range(M-days+1):
        cart = {}
        for j in range(days):
            item = discount[i + j]
            if item not in cart:
                cart[item] = 1
            else:
                cart[item] += 1
        
        if cart == want_dict:
            ans += 1

    return ans