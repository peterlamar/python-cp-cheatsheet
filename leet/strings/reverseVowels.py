class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = set('aeiouAEIOU')
        
        ans = list(s)
        
        while l<r:
            
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
            
            if s[l] in vowels and s[r] in vowels:
                ans[l],ans[r] = ans[r], ans[l]                
                l += 1
                r -= 1
        
        return "".join(ans)