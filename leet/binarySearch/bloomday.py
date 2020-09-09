"""
time: lgn
space: 1
"""
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def possible(days):
            b, f = 0, 0 
            for bm in bloomDay:
                if bm > days:
                    f = 0
                else:
                    f += 1
                    if f == k:
                        b += 1
                        f = 0
            return b >= m
        
        if len(bloomDay) < m * k:
            return -1
        
        l, r = min(bloomDay), max(bloomDay)
        
        while l < r:
            mid = l + r >> 1
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l