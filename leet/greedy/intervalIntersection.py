"""
time: a + b
space: a + b
"""
class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        rtn = []
        a = b = 0
        
        while a < len(l1) and b < len(l2):
            ast, aed = l1[a]
            bst, bed = l2[b]
            
            # if intersecting, merge. 
            if aed >= bst and ast <= bed:
                rtn.append((max(ast,bst), min(bed, aed)))
            
            # else catch up list using end times
            if aed <= bed:
                a += 1
            else:
                b += 1
        
        return rtn