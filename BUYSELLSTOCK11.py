def maxProfit(prices):
    start = 1
    last = 0
    l = len(prices)
    profit = 0
    while start < l:
        if prices[last] >= prices[start]:
            last = start 
            start += 1
        elif prices[start] > prices[last]:
            cur_profit = prices[start] - prices[last]
            if cur_profit > profit:
                profit = cur_profit
        start += 1        
    return profit            


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))   

