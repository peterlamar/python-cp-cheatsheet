class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = m = float('inf')
        
        for n in nums:
            if n <= l:
                l = n
            elif n <= m:
                m = n
            else:
                return True
    
        return False