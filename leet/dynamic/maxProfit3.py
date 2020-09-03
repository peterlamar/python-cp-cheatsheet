class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t0 = [0] * 3
        t1 = [float(-inf)] * 3
        
        for p in prices:
            for i in range(2,0,-1):
                t0[i] = max(t0[i], t1[i] + p)
                t1[i] = max(t1[i], t0[i-1] - p)
        
        return t0[2]
    