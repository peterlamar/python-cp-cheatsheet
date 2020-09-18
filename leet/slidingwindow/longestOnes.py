class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        cnt = 0
        
        for r in range(len(A)):
            K -= 1 - A[r]
                
            if K < 0:
                K += 1 - A[l]
                l += 1
            
        return r-l+1