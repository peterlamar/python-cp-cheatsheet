"""
time: lgn
space: 1
Kth Missing Positive Number
The number of positive integers which are missing
before the arr[idx] is equal to arr[idx] - idx - 1.
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = l + (r-l) // 2
            if arr[m] - 1 - m >= k:
                r = m
            else:
                l = m + 1
        return l + k

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        class Count(object):
            def __getitem__(self, i):
                return arr[i] - i - 1
        return k + bisect.bisect_left(Count(), k, 0, len(arr))