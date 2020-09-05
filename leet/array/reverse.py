class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(l, r, nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if len(nums) <= 1: return
        k = k % len(nums)
        reverse(0, len(nums)-1, nums)
        reverse(0, k-1, nums)
        reverse(k, len(nums)-1, nums)

        
            