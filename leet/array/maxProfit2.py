"""
time: 4 min
errors: none
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minPrice = float('inf')
        
        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p - minPrice)
                
        return maxProfit
