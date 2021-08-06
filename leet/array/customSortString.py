"""
time: nlogn
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ref = {c:i for i,c in enumerate(order)}
        s = list(s)
        s.sort(key = lambda x: ref[x] if x in ref else 27)
        return "".join(s)

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ct = collections.Counter(s)
        ans = []
        
        for c in order:
            ans.append(c * ct[c])
            ct[c] = 0
        
        for c in ct:
            ans.append(c * ct[c])
            
        return "".join(ans)