# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
"""
Correctly initialize the boundary variables left and right. 
Only one rule: set up the boundary to include all possible 
elements;

Decide return value. Is it return left or return left - 1?
Remember this: after exiting the while loop, left is the 
minimal k​ satisfying the condition function;

Design the condition function. This is the most difficult 
and most beautiful part. Needs lots of practice.

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
"""
class Solution:
    def firstBadVersion(self, n) -> int:
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left