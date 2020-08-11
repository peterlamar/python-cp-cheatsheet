"""
isPalindrome()

for c in s:
    is string without charactor a palindrome

    racecatr
    acecat
    aceca
    cecat

"""
"""

"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                leftTest = (s[left:right])
                leftTestRev = leftTest[::-1]
                if leftTest == leftTestRev:
                    return True
                
                rightTest = (s[left+1:right+1])
                rightTestRev = rightTest[::-1]
                if rightTest == rightTestRev:
                    return True
                
                return False
            left += 1
            right -= 1
        return True