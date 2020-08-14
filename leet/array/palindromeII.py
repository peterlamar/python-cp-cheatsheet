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
    def validPalindrome(self, s: str) -> bool:
  
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                # handle ba
                if left + 1 == right:
                    return True
                
                # handle abc
                # Test string 1
                stringA = s[left+1:right+1]
                revStringA = stringA[::-1]
                if stringA == revStringA:
                    return True
                                
                stringB = s[left:right]
                revStringB = stringB[::-1]
                if stringB == revStringB:
                    return True  
                
                return False
            left = left + 1
            right = right - 1
            
            
        return True
    
    
    