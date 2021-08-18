class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = collections.defaultdict(list)
        
        # Create adj graph of stops -> routes. so for [[1,2,7],[3,6,7]]
        # {1->0, 2->0, 7->0,1, etc}
        for i, r in enumerate(routes):
            for s in r:
                adj[s].append(i)
                
        # Navigate and see if we can get from source to dest
        dfs = [(source, 0)]
        seenStops = set()
        seenRoutes = set()
        
        
        for s, buses in dfs:
            if s == target:
                return buses
            
            for r in adj[s]:
                if r not in seenRoutes:
                    seenRoutes.add(r)
                    for s in routes[r]:
                        if s not in seenStops:
                            seenStops.add(s)
                            dfs.append((s, buses+1))
        return -1

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        adj = collections.defaultdict(set)
        
        for i, r in enumerate(routes):
            for stop in r:
                adj[stop].add(i)
        
        dfs = deque([(source, 0)])
        seenStops = {source}
        seenRoutes = set()
        
        while dfs:
            stop, busRoute = dfs.popleft()
            if stop == target:
                return busRoute
            for route in adj[stop]:
                if route not in seenRoutes:
                    seenRoutes.add(route)
                    for s in routes[route]:
                        if s not in seenStops:
                            seenStops.add(s)
                            dfs.append((s, busRoute+1))
        
        return -1