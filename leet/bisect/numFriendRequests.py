class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = 0
        ages.sort()
        for a in ages:
            idx1 = bisect.bisect(ages, a)
            idx2 = bisect.bisect(ages, 0.5*a+7)
            cnt += max(0, idx1-idx2-1)
        return cnt