"""
Return the minimum time in seconds to
visit all the points in the order given 
by points
"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cnt = 0
        sx, sy = points.pop()
        while points:
            px, py = points.pop()
            cnt += max(abs(sx-px), abs(sy-py))
            sx = px
            sy = py
        
        return cnt