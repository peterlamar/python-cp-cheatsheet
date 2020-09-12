"""
time: n
space: n
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        merged = [intervals[0]]
        
        for s,e in intervals[1:]:
            ms, me = merged[-1]
            if me >= s:
                merged[-1] = (ms, max(me,e))
            else:
                merged.append((s,e))
        
        return merged