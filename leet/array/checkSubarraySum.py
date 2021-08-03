"""
time: n
space: up to n
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # look for repeated mod values to signal multiple of k
        hm = {0:-1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            
            key = total % k
            
            # values not adjacent
            if key in hm:
                if i - hm[key] > 1:
                    return True
            else:
                hm[key] = i
        
        return False             