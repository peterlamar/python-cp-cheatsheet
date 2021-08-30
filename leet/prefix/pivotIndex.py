"""
[2, 1, -1]
rsum = 2
ps + n = 2
check lsum = rsum (2=2)
rsum -= n 
O(N) (2n)
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = 0
        rsum = sum(nums)
        
        for i, n in enumerate(nums):
            ps += n
            if ps == rsum:
                return i
            rsum -= n

        return -1