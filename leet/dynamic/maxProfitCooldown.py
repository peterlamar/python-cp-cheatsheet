class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t0, t1 = 0, float('-inf')
        
        t0old2 = 0
        
        for p in prices:
            t0old = t0
            t0 = max(t0, t1 + p)
            t1 = max(t1, t0old2 - p)
            t0old2 = t0old
        
        return t0