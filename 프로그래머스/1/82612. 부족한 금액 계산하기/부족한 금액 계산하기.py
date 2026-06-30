def solution(price, money, count):
    total = 0
    
    for i in range(count):
        total += (price + (price * i))
    
    if total > money:
        return abs(money - total)
    else:
        return 0