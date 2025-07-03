# Best Time to Buy and Sell Stock
def maxProfit(prices):
  max_profit = 0
  min_price = float('inf')

  for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

  return max_profit

prices = [7,1,5,3,6,4]
max_profit = maxProfit(prices)
print(max_profit)
