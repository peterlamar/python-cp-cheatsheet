"""
time: 5 min
errors: solved wrong problem
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = totalProfit = 0
        
        if len(prices) <= 1:
            return totalProfit

        minPrice = prices[0]
        for p in prices:
            profit = p - minPrice
            if profit > 0:
                totalProfit += profit
                minPrice = p
            else:
                minPrice = min(minPrice, p)
                
        return totalProfit
        