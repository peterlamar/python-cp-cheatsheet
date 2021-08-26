"""
Max Consecutive Ones III
O(N)
1
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # move right
        # if left > k, move left until 0
        l = 0
        rtn = 0
        
        for r, n in enumerate(nums):
            
            if n == 0:
                k -= 1
            
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            
            rtn = max(rtn, r-l+1)
            
        return rtn

    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        cnt = 0
        
        for r in range(len(A)):
            K -= 1 - A[r]
                
            if K < 0:
                K += 1 - A[l]
                l += 1
            
        return r-l+1