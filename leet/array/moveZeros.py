"""
time: n
space: 1
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i,n in enumerate(nums):
            if n != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1