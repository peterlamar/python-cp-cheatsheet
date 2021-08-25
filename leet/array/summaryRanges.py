class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        s = 0
        rtn = []
        
        if not nums:
            return
        
        def addStr(nums, s, i):
            if nums[s] == nums[i]:
                return f"{nums[s]}"
            else:
                return f"{nums[s]}->{nums[i]}"
        
        for i in range(0, len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                rtn.append(addStr(nums, s, i))
                s = i+1

        rtn.append(addStr(nums, s, len(nums)-1))


        return rtn
                