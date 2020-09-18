"""
time: O(nk)
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = collections.Counter()
        l = mx = 0
        
        for r, c in enumerate(s):
            cnt[c] += 1
            
            if len(cnt.keys()) > k:
                if cnt[s[l]] > 1:
                    cnt[s[l]] -= 1
                else:
                    del cnt[s[l]]
                l += 1
            
            mx = max(mx, r-l+1)
                
        return mx