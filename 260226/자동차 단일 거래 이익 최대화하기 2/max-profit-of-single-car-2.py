N = int(input())
lst = list(map(int, input().split()))

min_price = lst[0]
max_profit = 0

for price in lst[1:]:
    profit = price - min_price
    max_profit = max(profit, max_profit)

    min_price = min(min_price, price)

print(max_profit)