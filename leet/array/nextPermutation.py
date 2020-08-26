# find decreasing substring/max permutation
# iterate pivot with next highest number
# reverse substring to right of pivot
# time: 34 min first pass
# errors: lots of bugs, 
# did not handle 1,5,1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxDcr = float('-inf')
        maxI = 0
        dcr = False
        i = 0
        
        if len(nums) == 0 or len(nums) == 1:
            return
        
        # Get max num
        while i < len(nums):
            if maxDcr <= nums[i]:
                maxDcr = nums[i]
                maxI = i
            i += 1
        
        # If max, reverse then return
        if maxI == 0:
            i = 0
            while i < len(nums) // 2:
                end = len(nums) - 1 - i
                nums[i], nums[end] = nums[end], nums[i]
                i += 1
            return
        
        if maxI == len(nums) - 1:
            nums[maxI], nums[maxI-1] = nums[maxI-1], nums[maxI]
            return
        
        
        # Get next max num (TODO: if no nextMax)
        i = maxI + 1
        nextMax = float('-inf')
        nextMaxI = float('-inf')
        while i < len(nums):
            if nextMax <= nums[i]:
                nextMax = nums[i]
                nextMaxI = i
            i += 1
        
        # Swap pivots
        nums[maxI-1], nums[nextMaxI] = nums[nextMaxI], nums[maxI-1]
        
        #Reverse sub
        offset = maxI 
        i = offset
        
        while i < len(nums) - (len(nums) - offset) // 2:
            end = len(nums) - 1 - i + offset
            nums[i], nums[end] = nums[end], nums[i]
            i += 1
        
        return

"""
2nd round, must faster. 
More algorithm insights and use of built in reverse and while loops
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        
        # Get largest number index
        while i > 0 and nums [i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return
        
        # Get next smallest index
        j = len(nums) - 1
        k = i - 1
        while nums[k] > nums[j]:
            j -= 1
        
        # Swap pivots
        nums[i-1], nums[j] = nums[j], nums[i-1]
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
