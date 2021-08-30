class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hm = {0:-1}
        ps = rtn = 0
        
        for i, n in enumerate(nums):
            if n == 0:
                ps += -1
            else:
                ps += 1
            
            if ps in hm:
                rtn = max(rtn, i-hm[ps])
            else:
                hm[ps] = i
             
        return rtn
