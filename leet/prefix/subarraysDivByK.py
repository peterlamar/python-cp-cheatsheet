"""
arr  4   5   0  -2 -3   1
ps   4   9   9   7  4   5
ps%5 4   4   4   3  4   0
0=1
hm  4=1 4=2 4=3 3=1 4=4 0=2
1+2+3+1 = 7 Winning!
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rtn = ps = 0
        hm = collections.Counter([0])
        
        for i, n in enumerate(nums):
            ps += n
            rtn += hm[ps%k]
            hm[ps%k] += 1
        
        return rtn
                