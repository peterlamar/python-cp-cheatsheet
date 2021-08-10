class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        return cnt.most_common(1)[0][0]