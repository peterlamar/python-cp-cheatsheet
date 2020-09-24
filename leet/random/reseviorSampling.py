"""
time: init: 1, pick: n worst case
space: n, 1
"""
class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == 1:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)