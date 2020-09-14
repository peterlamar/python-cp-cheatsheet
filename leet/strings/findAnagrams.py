"""
time: c*26 + p
space: 26 + 26 (1)
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cntP = collections.Counter(p)
        cntS = collections.Counter()
        P = len(p)
        S = len(s)
        if P > S:
            return []
        ans = []
        for i, c in enumerate(s):
            cntS[c] += 1
            if i >= P:
                if cntS[s[i-P]] > 1:
                    cntS[s[i-P]] -= 1
                else:
                    del cntS[s[i-P]]
            if cntS == cntP:
                ans.append(i-(P-1))
        return ans