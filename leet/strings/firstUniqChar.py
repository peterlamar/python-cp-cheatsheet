class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter()
        
        for c in s:
            cnt[c] += 1
        
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1