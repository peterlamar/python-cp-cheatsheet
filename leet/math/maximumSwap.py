"""
time: n
space: n
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        lnum = list(str(num))
        max_idx = len(lnum) - 1
        min_idx = 0
        max_right = 0
        for i in range(len(lnum) - 2, -1, -1):
            if lnum[i] > lnum[max_idx]:
                max_idx = i
            elif lnum[i] < lnum[max_idx]:
                min_idx = i
                max_right = max_idx
        lnum[min_idx], lnum[max_right] = lnum[max_right], lnum[min_idx]
        return int("".join(lnum))