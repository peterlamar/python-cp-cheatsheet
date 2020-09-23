"""
time: n^2 for every matrix
space: n
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = set()
        
        def dfs(node):
            for nei, adj in enumerate(M[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        ans = 0
        for n in range(len(M)):
            if n not in seen:
                dfs(n)
                ans += 1
        
        return ans
            