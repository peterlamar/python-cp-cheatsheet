"""
time: n+ nlgk
space: n + k
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        return heapq.nsmallest(k, count, lambda x:(-count[x], x))
