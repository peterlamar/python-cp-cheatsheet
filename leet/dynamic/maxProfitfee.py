class Solution:
    """
           1  3  2 8 4 9
    t0     0  0  0 5 5 8 
    t0old  0  0  0 0 5 5
    t1    -1 -1 -1 0 1 1
    """
    def maxProfit(self, prices: List[int], fee: int) -> int:
        t0, t1 = 0, float('-inf')
        
        for p in prices:
            t0old = t0
            t0 = max(t0, t1 + p - fee)
            t1 = max(t1, t0old - p)
        
        return t0