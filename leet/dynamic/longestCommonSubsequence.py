"""
time: M*N 
space: M*N 
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        Y = len(text2)+1
        X = len(text1)+1
        dp = [[0] * Y for _ in range(X)]
        # [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                if c == d:
                    dp[i + 1][j + 1] = 1 + dp[i][j]  
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
# [[0,0,0,0],[0,1,1,1],[0,1,1,1],[0,1,2,2],[0,1,2,2],[0,1,2,3]]
# abcde
# "ace"