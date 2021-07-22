"""
time: n
space: l + l2 (non zero elements)
"""
class SparseVector:
    vec = {}
    
    def __init__(self, nums: List[int]):
        self.vec = {i:n for i,n in enumerate(nums) if n != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(vec.vec[i] * self.vec[i] for i in self.vec if i in vec.vec)


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)