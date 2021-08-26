"""
Find First and Last Position of Element in Sorted Array
time: 2lgn
"""
from bisect import bisect, bisect_left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = bisect.bisect_left(nums, target)
        e = bisect.bisect(nums, target) -1
        if s <= e:
            return [s,e]
        else:
            return [-1,-1]