"""
time: s(n) + target(n)lgn
space: s(n) 
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ref = collections.defaultdict(list)
        for i,c in enumerate(source):
            ref[c].append(i)
        
        ans = 1
        
        i = -1
        for c in target:
            if c not in ref:
                return -1
            
            offset = ref[c]
            j = bisect.bisect_left(offset, i)
            if j == len(offset):
                ans += 1
                i = offset[0] + 1
            else:
                i = offset[j] + 1
                
        return ans