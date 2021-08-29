"""
    0, 2, 0, 0, -2
    0, 2, 3, 0, 0
    -2       2
    -2 0. 3  5  3
    O(n + k)
"""

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        rtn = [0]*length
        
        for s,e,i in updates:
            rtn[s] += i
            if e+1 < len(rtn):            
                rtn[e+1] -= i
                
        rtn = itertools.accumulate(rtn)
        
        return rtn