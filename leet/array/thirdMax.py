"""
time: n
space: 1
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)
            if len(seen) > 3:
                seen.remove(min(seen))
        if len(seen) < 3:
            return max(seen)
        return min(seen)