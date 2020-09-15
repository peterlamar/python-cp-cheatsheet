"""
time: n
space: up to n
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dt = collections.defaultdict(int)
        dt[0] = -1
        
        if len(nums) <= 1:
            return False
        
        total = 0
        for i,n in enumerate(nums):
            total += n
            if k != 0:
                rem = total % k
            else:
                rem = total
            
            if rem in dt:
                if i - dt[rem] > 1:
                    return True
            else:
                dt[rem] = i
            
        return False                