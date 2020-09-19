"""
time: logn
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        
        while l<r:
            m = l + r >> 1
            if x - arr[m] <= arr[m+k]-x:
                r = m 
            else:
                l = m + 1
        
        return arr[l:l+k]