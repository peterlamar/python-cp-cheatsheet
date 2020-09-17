"""
time: nlogn
"""
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        m = {c:i for i, c in enumerate(S)}
        return ''.join(sorted(T, key=lambda x: m.get(x,  ord(x))))


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ct = collections.Counter(T)
        ans = []
        
        for c in S:
            ans.append(c * ct[c])
            ct[c] = 0
        
        for c in ct:
            ans.append(c * ct[c])
            ct[c] = 0
            
        return "".join(ans)