class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.nlargest(k, nums)
        return heap[-1]        