class Solution:

    # Longest Continuous Increasing Subsequence Subarray
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        rtn = cnt = 0
        
        for i, n in enumerate(nums):
            
            if i == 0 or n <= nums[i-1]:
                cnt = 0
            cnt += 1
            rtn = max(rtn, cnt)
    
        return rtn

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1]+1
        return max(dp)