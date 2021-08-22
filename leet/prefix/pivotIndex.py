class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r = sum(nums)
        ps = 0
        
        for l, n in enumerate(nums):
            ps += n
            if ps == r:
                return l
            r -= n
        
        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for i,n in enumerate(nums):
            right -= n
            if left == right:
                return i
            left += n
        return -1