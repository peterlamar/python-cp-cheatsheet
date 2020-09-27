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

"""
time: n^2
space: n
"""
class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        q = [0]
        visited = set()
        
        while q:
            i = q.pop()
            visited.add(i)
            for w in wordDict:
                wend = i+len(w)
                if s[i:wend] == w:
                    if wend == len(s):
                        return True
                    else:
                        if wend not in visited:
                            q.append(wend)
                            
        return False