"""
time: n^2 for every matrix
space: n
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = set()
        ans = 0
        
        def dfs(m):
            for nei, adj in enumerate(M[m]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
                
        
        for m in range(len(M)):
            if m not in seen:
                dfs(m)
                ans += 1
        
        return ans
            