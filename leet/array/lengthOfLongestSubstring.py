"""
 tmmzuxt
  i
       j
               
"""

class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength=0
        i = 0
        used = {}
        
        for j,c in enumerate(s):
            if c in used and i <= used[c]:
                # move i to after found char
                i = max(used[c]+1, i)
            else:
                maxlength = max(maxlength, j-i+1,)
                
            used[c] = j

        return maxlength