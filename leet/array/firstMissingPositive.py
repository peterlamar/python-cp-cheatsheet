class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        
        for n in nums:
            s.add(n)

        # 1, 2, 3, 4
        for i in range(1, len(nums)):
            if i not in s:
                return i

        if len(nums) not in s:
            return len(nums)
        
        return len(nums) + 1