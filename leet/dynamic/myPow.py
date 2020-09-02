"""
time: 20 min
time: O(log(n))
space: O(1)
Fast Power Algorithim/Exponential by squaring
https://en.wikipedia.org/wiki/Exponentiation_by_squaring
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = abs(n)
        ans = 1
        
        while p > 0:
            if p % 2 == 1:
                ans = ans * x
            x *= x
            p = p // 2
        
        if n < 0:
            ans = 1/ans
        
        return ans