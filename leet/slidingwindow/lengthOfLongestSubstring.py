"""
 tmmzuxt
  i
       j
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rtn = 0
        hm = {}
        l = 0
        
        for r, c in enumerate(s):
            if c in hm and l <= hm[c]:
                l = max(hm[c]+1, l)
            
            hm[c] = r

            rtn = max(rtn, r-l+1)

        return rtn

