"""
time: 17 min
errors:
off by one with slice s[mj:mi]
forgot to move failure pointer
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        j = 0
        matched = 0
        ht = {}
        minRes = float('inf')
        mi = mj = 0
        
        
        for c in t:
            ht[c] = ht.get(c, 0) + 1
        
        for i, c in enumerate(s):
            if c in ht:
                ht[c] -= 1
                if ht[c] == 0:
                    matched += 1
            
            if matched == len(ht):
                if i - j + 1 < minRes:
                    minRes = i - j + 1
                    mi = i + 1
                    mj = j
        
            while matched == len(ht):
                jc = s[j]
                
                if matched == len(ht):
                    if i - j + 1 < minRes:
                        minRes = i - j + 1
                        mi = i+1
                        mj = j
                
                if jc in ht:
                    if ht[jc] == 0:
                        matched -= 1
                    ht[jc] += 1
                j += 1
        
        if mi == 0 and mj == 0:
            return ''
        
        return s[mj:mi]