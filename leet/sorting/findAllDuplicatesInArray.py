class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        rtn = []
        
        for n in nums:
            if nums[abs(n)-1] < 0:
                rtn.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
                
        return rtn