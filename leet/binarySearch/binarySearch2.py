class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid 
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid 
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target