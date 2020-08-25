"""
time: over 1 hour
Errors: too many, tried to apply template
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ht = {}
        l = 0
        matched = 0
        
        for c in s1: 
            ht[c] = ht.get(c, 0) + 1
        
        for r, c in enumerate(s2):
            if c in ht:
                ht[c] -= 1
                if ht[c] == 0:
                    matched += 1
                    
            if matched == len(ht):
                return True
                
            if r >= len(s1) - 1:
                lc = s2[l]
                l += 1
                if lc in ht:
                    if ht[lc] == 0:
                        matched -= 1
                    ht[lc] += 1
        
        return False
        