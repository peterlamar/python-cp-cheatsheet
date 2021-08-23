class Solution:

    def maxLength(self, ribbons: List[int], k: int) -> int:            
        
        total = sum(ribbons)
        if k > total:
            return 0
        
        l, r = 0, 100001
        while l < r:
            m = l + (r-l) // 2
            if sum(r//m for r in ribbons) < k:
                r = m
            else:
                l = m + 1
        return l-1

    def maxLength(self, ribbons: List[int], k: int) -> int:
        # return True if we can gert x ribbons of length k
        total = sum(ribbons)
        
        if k > total:
            return 0
        
        def check(m: int):
            tot = 0
            for r in ribbons:
                tot += r // m
            if k > tot:
                return True
            return False
        
        rtn = 0 
        l, r = 1, 100001
        while l < r:
            m = l + (r-l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l-1