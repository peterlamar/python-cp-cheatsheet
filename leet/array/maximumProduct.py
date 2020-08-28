class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l = heapq.nlargest(3, nums)
        s = heapq.nsmallest(3, nums)
        return max(l[0]*l[1]*l[2],s[0]*s[1]*l[0])
