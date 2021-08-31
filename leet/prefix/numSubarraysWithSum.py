class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = collections.Counter([0])
        rtn = ps = 0
        
        for n in nums:
            ps += n
            rtn += cnt[ps-goal]
            cnt[ps] += 1
        
        return rtn