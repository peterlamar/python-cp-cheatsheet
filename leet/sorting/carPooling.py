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