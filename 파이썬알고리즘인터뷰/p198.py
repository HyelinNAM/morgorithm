# 한 번의 거래로 낼 수 있는 최대 이익 산출

# 혜린
def best_profit(prices):

    min = prices[0]
    profit = 0

    for price in prices:

        if price <= min:
            min = price

        elif min < price:
            if (price-min) <= profit:
                pass

            else:
                profit = price-min

        # ↑ min, max로 구현하기.
    return profit

# 책

import sys

def best_profit(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)

    return profit

prices = [7,1,5,3,6,4]
best_profit(prices)

