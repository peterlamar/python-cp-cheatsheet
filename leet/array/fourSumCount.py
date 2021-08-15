class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = collections.Counter(a+b for a in nums1 for b in nums2)
        return sum(cnt[-c-d] for c in nums3 for d in nums4)

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        rtn = 0
        cnt = collections.Counter()
        for a in nums1:
            for b in nums2:
                cnt[a+b] += 1
        
        for c in nums3:
            for d in nums4:
                rtn += cnt[-c-d]
        
        return rtn