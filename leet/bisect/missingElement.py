"""
time: lgn
space: 1
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        target = k + nums[0] - 1
        left_element = bisect.bisect(nums, target)
        while left_element:
            nums = nums[left_element:]
            target += left_element
            left_element = bisect.bisect(nums, target)
        return target