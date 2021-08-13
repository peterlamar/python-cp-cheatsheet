class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        
        for fr, to in sorted(tickets)[::-1]:
            adj[fr].append(to)
            
        rtn = []
        def visit(airport):
            while adj[airport]:
                visit(adj[airport].pop())
            rtn.append(airport)
        
        visit('JFK')
                    
        return rtn

                    
