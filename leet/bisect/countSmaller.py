"""
time: n^2 worst case
space: 2n
"""
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        seen = []
        rtn = [0] * N
        for i in range(N-1,-1,-1):
            j = bisect.bisect_left(seen, nums[i])
            rtn[i] = j
            bisect.insort(seen, nums[i])
        return rtn