"""
time: n
space: 1
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        
        if N == 0:
            return
        
        i = 0
        while i < N:
            if nums[i] == val:
                del nums[i]
                N -= 1
            else:
                i += 1
        
        return N + 1
        