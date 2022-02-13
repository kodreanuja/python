def maxProfit(prices):
    return sum(max(0, x) for x in (y - x for x, y in zip(prices,prices[1:])))
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))   
  