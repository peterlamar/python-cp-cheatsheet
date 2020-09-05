class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        mx = set()
        for n in nums:
            mx.add(n)
            if len(mx) > 3:
                mset = min(mx)
                mx.remove(mset)
        if len(mx) < 3:
            return max(mx)
        return min(mx)
                