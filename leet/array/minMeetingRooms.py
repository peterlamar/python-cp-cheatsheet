"""
time: 19 min
errors: none but peeked at solution to confirm counting algo
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []
        rooms = 0        
        maxRooms = 0
        
        if len(intervals) <= 1:
            return len(intervals)
        
        for m in intervals:
            starts.append(m[0])
            ends.append(m[1])
        
        starts.sort()
        ends.sort()

        
        eid = 0
        sid = 0
        while sid < len(starts) and eid < len(ends):
            if starts[sid] < ends[eid]:
                sid += 1
                rooms += 1
            else:
                eid += 1
                rooms -= 1
            maxRooms = max(maxRooms, rooms)
        
        return maxRooms