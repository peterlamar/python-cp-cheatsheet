"""
time: k * p
space: p
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0
        
        dp = [0] * len(prices)
        
        if k > len(prices):
            profit = 0
            for i in range(1, len(prices)):
                profit = max(profit, profit + prices[i] - prices[i-1])
            return profit
                
        for _ in range(k):
            val = 0
            for i in range(1, len(prices)):
                val = max(dp[i], val + prices[i]-prices[i-1])
                dp[i] = max(val, dp[i-1])

        return dp[-1]

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= k:
            t0, t1 = 0, float(-inf)
            for p in prices:
                t0old = t0
                t0 = max(t0, t1 + p)
                t1 = max(t1, t0old - p)
            return t0
        
        t0 = [0] * (k+1)
        t1 = [float(-inf)] * (k+1)
        
        for p in prices:
            for i in range(k, 0, -1):
                t0[i] = max(t0[i], t1[i] + p)
                t1[i] = max(t1[i], t0[i-1] - p)
                
        return t0[k]