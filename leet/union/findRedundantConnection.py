class DSU:
    def __init__(self, N):
        self.par = list(range(N))

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.par[yr] = xr
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        N = len(edges)
        dsu = DSU(1001)
        for edge in edges:
            x = edge[0]
            y = edge[1]
            if dsu.union(x,y) == False:
                return edge
            

                
            
        
