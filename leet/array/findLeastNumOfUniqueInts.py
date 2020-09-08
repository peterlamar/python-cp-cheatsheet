class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        sfreqs = sorted(count.values())
        
        ans = len(sfreqs)
        for f in sfreqs:
            if k >= f:
                k -= f
                ans -= 1
        
        return ans
                
        