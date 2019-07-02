def maxProfitV1(prices):
    # wrong implementation
    # this returns the day not the profit
    # this is n^2


    index1, index2 = 0, 1
    max = len(prices) - 1
    # profit = {} # cache?
    day = 0
    max_profit = 0
    while index1 < max:
        if index2 > max:
            index1 += 1
            index2 = index1 + 1
        else:
            price1 = prices[index1]
            price2 = prices[index2]
            profit = price2 - price1

            if profit > max_profit:
                max_profit = profit
                day = index2 + 1
            elif price1 > price2:
               "no profit"

            index2 = index2 + 1

    return day

def maxProfitV2(prices):
    # You need to find the min max for the array.
    # More specifically, you need to find the smallest price followed by max profit.
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price


    return max_profit

