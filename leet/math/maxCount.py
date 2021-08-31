"""
m = 3, n = 3, ops = [[2,2],[3,3]]
Min columns and rows get multiplied the most
"""
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minCol = m
        minRow = n
        
        for c, r in ops:
            minCol = min(minCol, c)
            minRow = min(minRow, r)
        
        return minCol * minRow
