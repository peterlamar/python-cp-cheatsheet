class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] * (len(nums)+1)
        
        for i, n in enumerate(nums):
            self.nums[i+1] = self.nums[i] + n
            
        print(self.nums)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:

    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        
        self.nums = nums
        print(nums)
        
    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.nums[right] - self.nums[left-1]
        else:
            return self.nums[right]
        return 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)