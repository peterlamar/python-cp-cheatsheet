class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # delete min of hm.values()
        l = 0
        hm = {}
        rtn = 0
        
        for r, c in enumerate(s):
            hm[c] = r
            
            if len(hm) > 2:
                idx = min(hm.values())
                del hm[s[idx]]
                l = idx + 1
            
            rtn = max(rtn, r-l+1)
            
        return rtn
            