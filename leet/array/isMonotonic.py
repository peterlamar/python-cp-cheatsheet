class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        up = down = True
        
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                up = False

            if A[i - 1] < A[i]:
                down = False
        
        return up or down