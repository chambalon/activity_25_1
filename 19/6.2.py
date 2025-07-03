# Best Time to Buy and Sell Stock using sliding window method
def maxProfit(prices):
  left = 0
  right = 1
  max_profit = 0
  

  for r in range(1, len(prices)):
    if prices[r] - prices[left] > 0 :
      max_profit = max(max_profit, prices[r] - prices[left])
    else:
      left = r

  return max_profit

prices = [7,1,5,3,6,4]
max = maxProfit(prices)
print(max)