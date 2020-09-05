"""
time: p * logk
space: k
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for p in points:
            distance = sqrt(p[0]* p[0] + p[1]*p[1])
            heapq.heappush(heap,(-distance, p))
            if len(heap) > K:
                heapq.heappop(heap)            
        return ([h[1] for h in heap])

def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:    
    return heapq.nsmallest(K, points, lambda x: x[0]*x[0] + x[1]*x[1])

        
class Solution:
    def kClosest(self, points, K):
        self.sort(points, 0, len(points)-1, K)
        return points[:K]
    
    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p+1, r, K)
            else:
                self.sort(points, l, p-1, K)
            
    def partition(self, points, l, r):
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]                
        return a