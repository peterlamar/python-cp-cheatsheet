"""
time: 5 min
errors: forgot range needed len to process list!
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rtn = [0] * len(nums)
        
        if len(nums) <= 1:
            return nums
        
        cur = 1
        for i in range(len(nums)):
            rtn[i] = cur
            cur *= nums[i]
        
        cur = 1
        for i in reversed(range(len(nums))):
            rtn[i] *= cur
            cur *= nums[i]
        
        return rtn