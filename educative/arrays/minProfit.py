def buy_and_sell_stock_once(prices):
  minPrice = float('inf')
  maxProfit = 0

  for p in prices:
    minPrice = min(minPrice, p)
    maxProfit = max(maxProfit, p - minPrice)

  return maxProfit