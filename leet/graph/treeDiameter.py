"""
time: n
space: n
"""
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        def dfs(curr, prev):
            mx1, mx2 = 0,0
            for nei in adj[curr]:
                if nei != prev:
                    d = dfs(nei, curr)
                    if d > mx1:
                        mx1, mx2 = d, mx1
                    elif d > mx2:
                        mx2 = d
            self.mxPath = max(self.mxPath, mx1 + mx2)
            return mx1+1
        
        self.mxPath = 0
        dfs(0, None)
        return self.mxPath