class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        dif = c1 & c2
        return list(dif.elements())
            
            
