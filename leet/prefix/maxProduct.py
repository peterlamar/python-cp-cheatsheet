class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = nums
        B = nums[::-1]
        for i in range(1, len(nums)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(A + B)