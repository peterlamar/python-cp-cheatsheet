class Solution:
    def numDecodings(self, s: str) -> int:
        # Count possibilities up to that point
        dp = [0] * (len(s) + 1 )
        
        dp[0] = 1
        dp[1] = 1 if s[0] !='0' else 0
        
        for i in range(2, len(s)+1):

            if  0< int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1] 
            
            if  9 < int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]

        return dp[len(s)]

    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, len(s)+1):
            if 0 < int(s[i-1:i]) < 10:
                dp[i] += dp[i-1]
            
            if 9 < int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]
            
        return dp[len(s)]