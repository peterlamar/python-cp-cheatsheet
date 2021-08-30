"""
time: n
space: up to n
Continuous Subarray Sum

Edge Case:
else:
    hm[ps%k] = i

       [5, 0, 0, 0]
ps      5  5. 5. 5
mod3    2  
           2
              2(T)
Because 0 is considered a multiple of k           
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # look for repeated mod values to signal continous subarrays
        # that are a multiple of k
        hm = {0:-1}
        
        ps = 0
        
        for i, n in enumerate(nums):
            ps += n
            
            if ps%k in hm:
                # Values not adjacent
                if i - hm[ps%k] > 1:
                    return True
            else:
                hm[ps%k] = i
        
        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # look for repeated mod values to signal multiple of k
        hm = {0:-1}
        ps = 0
        
        for i, n in enumerate(nums):
            ps += n
            key = ps%k
            if key in hm:
                # Values not adjacent
                if i - hm[key] > 1:
                    return True
            else:
                hm[key] = i
        
        return False