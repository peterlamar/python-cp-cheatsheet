"""
time: a
space: a
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(n*n for n in nums)