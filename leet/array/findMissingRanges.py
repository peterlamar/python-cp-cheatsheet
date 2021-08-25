class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        rtn = []
        
        for l, u in zip(nums, nums[1:]):
            if l + 2 == u:
                rtn.append(f"{l+1}")
            elif l + 2 < u:
                rtn.append(f"{l+1}->{u-1}")
        
        return rtn