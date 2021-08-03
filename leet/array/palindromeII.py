"""
isPalindrome()

for c in s:
    is string without charactor a palindrome

    racecatr
    i      j
    if true, i++, j--

    racecatr
    i.    j
    
    if false, continue with i+1 and j-1
    
    
    acecat
    aceca
    cecat

    abc
"""
"""

"""
class Solution:
    def validPalindrome(self, s:str)-> bool:
        l = 0
        r = len(s)-1
        
        while l < r:
            if s[l] != s[r]:
                
                # Handle aaabaa
                if l + 1 == r:
                    return True
                
                strA = s[l+1:r+1]
                if strA == strA[::-1]:
                    return True
                
                strB = s[l:r]
                if strB == strB[::-1]:
                    return True
                
                # handle aba
                return False
                
            l = l + 1
            r = r - 1

        # Normal palindrome func
        return True #
