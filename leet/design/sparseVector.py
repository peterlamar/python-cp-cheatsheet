"""
time: n
space: l + l2 (non zero elements)
"""
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

class SparseVector:
    def __init__(self, nums :List[int]):
        self.data = {i:n for i,n in enumerate(nums) if n != 0}
        return
    
    def dotProduct(self, vec : 'SpareVector') -> int:        
        # iterate through keys -for i in vec.data . Not for i,j in enumerate(vec.data)
        return sum([self.data[i] * vec.data[i] for i in vec.data if i in self.data])
    

class SparseVector:
    def __init__(self, nums: List[int]):
        self.ref = {}
        for i, n in enumerate(nums):
            self.ref[i] = n
    
    def dotProduct(self, sv: 'SparseVector') -> int:
        total = 0
        for k in sv.ref:
            if k in self.ref:
                total += self.ref[k] * sv.ref[k]
                
        return total
