"""
time: a + b
space: a + b
"""
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        a = 0
        b = 0
        rtn = []
        
        while a < len(A) and b < len(B):
            ast, ae =  A[a]
            bst, be =  B[b]
            
            if ast <= be and ae >= bst:
                rtn.append((max(bst, ast), min(ae,be)))
            
            if ae <= be:
                a += 1
            else:
                b += 1
        
        return rtn