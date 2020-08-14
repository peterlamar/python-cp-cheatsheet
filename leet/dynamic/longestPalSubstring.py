
"""
            b a b a d : start (x)
            0 1 2 3 4
        b 0 T F F F F
        a 1 F T F F F
        b 2 T F T F F
        a 3 F T F T F
        d 4 F F F F T
        :
        start (y)   
        
        
        1,3
        start (1)
        end (3)
        
        If top right is T, then I am a palindrome of length + 2
        
        
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[False] * n  for _ in range(n)]
        
        ans = ''
        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            
        maxLen = 1
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):             
				# palindrome condition
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if end - start + 1 > maxLen:
                            maxLen = end - start + 1
                            ans = s[start:end+1]
        return ans