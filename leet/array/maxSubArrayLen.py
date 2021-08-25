class Solution:
    # Maximum Size Subarray Sum Equals k
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hm = {0:-1}
        ps = 0
        rtn = 0
        for i in range(len(nums)):
            ps += nums[i]
            if ps not in hm:
                hm[ps] = i
            
            if ps - k in hm:
                rtn = max(rtn, i-hm[ps-k])
        
        return rtn

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        hm = {0:-1}
        ps = rtn = 0
        
        for i, n in enumerate(nums):
            ps += n
            
            if ps not in hm:
                hm[ps] = i
            
            if ps-k in hm:
                rtn = max(rtn, i-hm[ps-k])
        
        return rtn