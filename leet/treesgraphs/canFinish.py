class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        degrees = collections.Counter()
        
        for p in prerequisites:
            dest, orig = p
            adj[orig].append(dest)
            degrees[dest] += 1
            if orig not in degrees:
                degrees[orig] = 0
        
        stk = list(filter(lambda x:degrees[x]==0, degrees.keys()))
        cnt = len(stk)
        
        while stk:
            node = stk.pop()
            for nei in adj[node]:
                degrees[nei] -= 1
                if degrees[nei] == 0:
                    stk.append(nei)
                    cnt += 1
        
        return (cnt + numCourses - len(degrees)) == numCourses


