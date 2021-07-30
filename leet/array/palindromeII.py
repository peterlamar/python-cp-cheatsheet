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

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        
        while l<r:
            if s[l] != s[r]:
                if l + 1 == r:
                    return True
                
                sA = s[l:r]
                if sA == sA[::-1]:
                    return True
                
                sB = s[l+1:r+1]
                if sB == sB[::-1]:
                    return True    
                
                return False
            
            l = l + 1
            r = r - 1
            
        return True

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        
        while l<r:
            if l+1 == r:
                return True
            
            if s[l] != s[r]:
                a1 = s[l:r]
                if a1 == a1[::-1]:
                    return True
                
                a2 = s[l+1:r+1]
                if a2 == a2[::-1]:
                    return True
                
                return False
            
            l += 1
            r -= 1
        
        return True
        
            