class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = collections.defaultdict(set)
        
        for i, r in enumerate(routes):
            for stop in r:
                adj[stop].add(i)
        
        dfs = [(source, 0)]
        seenStops = set([source])
        seenRoutes = set()
        
        for stop, busRoute in dfs:
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