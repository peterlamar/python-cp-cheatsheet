"""
time: > 20 min
errors: misplaced :, new algo
time: O(logN)
space: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        l,r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            
            c = False
            if target <= nums[right]:
                if nums[mid] > nums[right]:
                    c = False
                else:
                    c = target <= nums[mid]
            else:
                if nums[mid] < nums[right]:
                    c = True
                else:
                    c = target <= nums[mid]
                    
            if c:
                r = mid
            else:
                l = mid + 1
                
        if nums[l] == target:
            return l
        else:
            return -1