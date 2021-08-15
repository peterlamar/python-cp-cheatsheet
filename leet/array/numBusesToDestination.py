class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stopToRoute = collections.defaultdict(set)
        
        for i, stops in enumerate(routes):
            for stop in stops: 
                stopToRoute[stop].add(i)
                
        bfs = [(source,0)]
        seenStops = {source}
        seenRoutes = set()
        
        for stop, buses in bfs:
            if stop == target:
                return buses
            
            for r in stopToRoute[stop]:
                if r not in seenRoutes:
                    seenRoutes.add(r)
                    for nextStop in routes[r]:
                        if nextStop not in seenStops:
                            seenStops.add(nextStop)
                            bfs.append((nextStop, buses+1))
        
        return -1