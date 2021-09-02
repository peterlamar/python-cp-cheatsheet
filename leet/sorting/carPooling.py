class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hm = collections.Counter()
        
        for c, s, e in trips:
            hm[s] += -c
            hm[e] += c

        for i in sorted(hm):
            capacity += hm[i]
            if capacity < 0:
                return False
        
        return True

"""
time: O(nlogn)
space: O(n)
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        
        for c, s, e in trips:
            heapq.heappush(heap, (e, -c))
            heapq.heappush(heap, (s, c))
        
        while heap:
            capacity -= heapq.heappop(heap)[1]
            if capacity < 0:
                return False
            
        return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        
        for c, s, e in trips:
            stops[s] += c
            stops[e] -= c
        
        return all(x <= capacity for x in itertools.accumulate(stops))