"""
time: 17 min
errors: missed corner case [1,1]
Did not get final insight into problem
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = i = 1
        currentJ = 0
        
        if len(nums) <= 2:
            return len(nums)
        
        currentJ = nums[j]
        while i < len(nums):
            if currentJ < nums[i]:
                nums[j] = nums[i]    
                currentJ = nums[i]
                j += 1
            i += 1
        
        return j

"""
time: 4 min
errors: none, had algo insight
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 0
        
        while i < len(nums):
            if nums[j] < nums[i]:
                j += 1
                nums[j] = nums[i]
            i += 1
        
        return j + 1