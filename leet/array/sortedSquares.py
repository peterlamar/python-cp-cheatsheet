"""
time: a
space: a
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        dq = deque()
        l = 0
        r = len(A)-1
        while l <= r:
            ls = A[l] ** 2
            rs = A[r] ** 2
            if ls >= rs:
                dq.appendleft(ls)
                l += 1
            else:
                dq.appendleft(rs)
                r -= 1
        return dq
            