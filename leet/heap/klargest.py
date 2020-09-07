"""
time: nlogk
logk add
space: k
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pool = []
        
        for n in nums:
            heapq.heappush(self.pool, n)
            if len(self.pool) > self.k:
                heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        heapq.heappush(self.pool, val)
        if len(self.pool) > self.k:
            heapq.heappop(self.pool)

        return self.pool[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)