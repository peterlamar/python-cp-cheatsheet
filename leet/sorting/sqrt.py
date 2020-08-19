"""
 4
1 4 
 2 
 
8
1 8
 4 F
 
12345678 
FFTTTTTT

k^2 > x, k-1 is solution
"""

class Solution:
    
    def mySqrt(self, x: int) -> int:
        def condition(value, x) -> bool:
            return value * value > x
        
        if x == 1:
            return 1

        left, right = 1, x
        while left < right:
            mid = left + (right-left) // 2
            if condition(mid, x):
                right = mid
            else:
                left = mid + 1
        return left - 1


    