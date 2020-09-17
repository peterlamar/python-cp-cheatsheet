class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = collections.defaultdict(set)
        emToName = {}
        
        for a in accounts:
            name = a[0]
            for em in a[1:]:
                first = a[1]
                adj[em].add(first)
                adj[first].add(em)
                emToName[em] = name

        seen = set()
        ans = []
        for email in adj:
            if email not in seen:
                seen.add(email)
                stk = [email]
                fd = []
                while stk:
                    node = stk.pop()
                    fd.append(node)
                    for nei in adj[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stk.append(nei)
                ans.append([emToName[email]] + sorted(fd))
        return ans
                
class DSU:
    def __init__(self):
        self.par = {}

    def find(self, x):
        if x != self.par.setdefault(x, x):
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        self.par[yr] = xr
        
class Solution:

    def accountsMerge(self, accounts):
        dsu = DSU()
        em_to_name = {}

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                dsu.union(acc[1], email)
        
        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(email)].append(email)
        
        return [[em_to_name[row[0]]] + sorted(row) for row in ans.values()]