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

# Quicksort
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def sort(arr, l, r):
            if l < r:
                p = part(arr, l, r)
                if p == K:
                    return
                elif p > K:
                    sort(arr, l, p-1)
                else:
                    sort(arr, p+1, r)
        
        def part(arr, l, r):
            pivot = arr[r]
            a = l
            for i in range(l, r):
                if arr[i][0]**2 + arr[i][1]**2 < pivot[0]**2 + pivot[1]**2:
                    arr[i], arr[a] = arr[a], arr[i]
                    a += 1
            arr[r], arr[a] = arr[a], arr[r]
            return a
        
        sort(points, 0, len(points)-1)
        return points[:K]