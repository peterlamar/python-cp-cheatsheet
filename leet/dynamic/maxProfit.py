class Solution:
    # buy sell stock one time
    def maxProfit(self, prices: List[int]) -> int:
        t0, t1 = 0, float('-inf')
        
        for p in prices:
            t0 = max(t0, t1 + p)
            t1 = max(t1, -p)
        
        return t0