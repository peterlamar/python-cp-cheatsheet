"""
time: n
space: (1)n
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(collections.Counter(tasks).values())
        mxCnt = max(task_counts)
        numTsks = task_counts.count(mxCnt)
        return max(len(tasks), (mxCnt-1)*(n+1) + numTsks)