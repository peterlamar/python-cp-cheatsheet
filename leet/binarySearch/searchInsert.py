"""
1356 : 5
FFTT : 2

1345 : 2
FTTT : 1

1345: 7
FFFF: 4 (list length)

1345: 0
TTTT: 0

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left