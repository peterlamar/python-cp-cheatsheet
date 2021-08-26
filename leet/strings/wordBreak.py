"""
time: n^2
space: n
"""
class Solution:
    # go through word and check if slice matches subword, go until the end
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        stk = [0]
        visited = set()
        
        while stk:
            i = stk.pop()
            visited.add(i)
            # check slice at index i
            for w in wordDict:
                wend = i + len(w)
                if s[i:wend] == w:
                    # return if we reach the end of s
                    if i + len(w) == len(s):
                        return True
                    if wend not in visited:
                        stk.append(wend)
        
        return False

"""
time: n^3
space: n
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for w in wordDict:
                if s[:i].endswith(w):
                    dp[i] |= dp[i-len(w)]
        return dp[-1]