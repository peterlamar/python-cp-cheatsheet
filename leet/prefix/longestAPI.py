class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hm = {0:-1}
        ps = rtn = 0
        
        for i, h in enumerate(hours):
            if h > 8:
                ps += 1
            else:
                ps -= 1
            
            hm.setdefault(ps, i)
            
            if ps > 0:
                rtn = max(rtn, i+1)
            
            if ps - 1 in hm:
                rtn = max(rtn, i-hm[ps-1])
            
        return rtn