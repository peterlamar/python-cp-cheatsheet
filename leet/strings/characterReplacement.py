class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sc = collections.Counter()
        l = 0
        
        if len(s) == 0:
            return 0
        
        for r, c in enumerate(s):
            sc[c] += 1
            mc = max(sc.values())
            sub = r - l + 1
            if sub - mc > k:
                sc[s[l]] -= 1
                l += 1

        return r-l+1
                
            
            