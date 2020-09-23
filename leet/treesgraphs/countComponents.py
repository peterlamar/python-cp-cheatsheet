class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        
    def find(self, x):
        if x != self.par[x]:        
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        self.par[yr] = xr
        return True
    
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        
        for e in edges:
            dsu.union(e[0], e[1])
            
        return len({dsu.find(x) for x in dsu.par})


class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return False
        self.par[yr] = xr
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        vs = set()
        
        for e in edges:
            dsu.union(e[0], e[1])
            vs.add(e[0])
            vs.add(e[1])
            
        st = set()
        
        for e in edges:
            st.add(dsu.find(e[0]))
            
        return len(st) + (n - len(vs))