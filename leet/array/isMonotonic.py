class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        up = down = True
        
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                up = False

            if nums[i - 1] < nums[i]:
                down = False
        
        return up or down