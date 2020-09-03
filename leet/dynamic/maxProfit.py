class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t0 = 0
        t1 = float('-inf')
        
        for p in prices:
            t0 = max(t0, t1 + p)
            t1 = max(t1, -p)
        
        return t0