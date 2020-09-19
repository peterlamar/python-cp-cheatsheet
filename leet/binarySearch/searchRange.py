"""
time: 2lgn
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = bisect.bisect_left(nums, target)
        e = bisect.bisect(nums, target)-1
    
        if 0 <= s <= e:
            return [s, e]
        else:
            return [-1, -1]