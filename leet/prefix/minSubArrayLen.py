"""
     [2,3,1,2,4 , 3]
ps    2 5 6 8 12 15
ps-7   -2-1 1 5  8

11
        0, 1, 2, 3, 4
       [1, 2, 3, 4, 5 ]
ps      1  3  6  10 15
       15, 5
       14, 4
       12, 3


        0, 1, 2
       [1, 4, 4]
ps      1  5, 9
        

"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = ps = 0
        rtn = len(nums)+1
        
        for r, n in enumerate(nums):
            ps += n
            
            while ps >= target and l<=r:
                rtn = min(rtn, r-l+1)
                ps -= nums[l]
                l += 1
        
        if rtn == len(nums)+1:
            return 0
        
        return rtn
            