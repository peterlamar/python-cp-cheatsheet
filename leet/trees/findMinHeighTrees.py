class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        
        if n == 1: return [0]
        
        # build adj graph
        for f, t in edges:
            adj[f].append(t)
            adj[t].append(f)
        
        # start with leeves
        leeves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leeves.append(i)
        
        # trim down leeves until we get to centoids
        # there can be one or two centoids
        while n > 2:
            n -= len(leeves)
            
            newLeeves = []
            for l in leeves:
                t = adj[l].pop()
                adj[t].remove(l)
                if len(adj[t]) == 1:
                    newLeeves.append(t)
            leeves = newLeeves
            
        return leeves
