class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def findKSum(nums : List[int], target: int, K: int, tmp: List[int], rtn: List[int]):
            if len(nums) < K or K < 2 or target < nums[0] * K or target > nums[-1]*K: # Early termination optimizations
                return
            
            # 2 sum
            if K == 2:
                l = 0
                r = len(nums)-1
                while l<r:
                    if nums[l] + nums[r] == target:
                        rtn.append(tmp + [nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
                        
            else:
                for i in range(0, len(nums)-K+1):
                    if i == 0 or i > 0 and nums[i-1] != nums[i]:
                        findKSum(nums[i+1:], target-nums[i], K-1, tmp+[nums[i]], rtn)
            return

        nums.sort()
        rtn = []
        findKSum(nums, target, 4, [], rtn)
        return rtn