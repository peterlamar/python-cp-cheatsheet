class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        
        if abs(S-T) > 1:
            return False
        
        for i in range(min(S, T)):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i+1:] == t[i:] or s[i:] == t[i+1:]
        
        if abs(S-T) == 1:
            return True
        
        return False