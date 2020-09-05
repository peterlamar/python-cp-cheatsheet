class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return heapq.nsmallest(k, freq.keys(), lambda x:(-freq[x], x))