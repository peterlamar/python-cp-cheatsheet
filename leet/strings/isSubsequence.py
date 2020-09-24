"""
time: O(t)
space: O(1)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
            
        sp = 0
        
        for tp in t:
            if s[sp] == tp:
                sp += 1
            if sp == len(s):
                return True
        
        return sp == len(s) 