class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        degree = collections.Counter()
        
        for p in prerequisites:
            dest, org = p
            adj[org].append(dest)
            degree[dest] += 1
            if org not in degree:
                degree[org] = 0
        
        free = set(range(numCourses)) - set(degree)
        for f in free:
            degree[f] = 0
        
        for i in range(len(degree), numCourses):
            if i not in degree:
                degree[i] = 0
        
        stk = list(filter(lambda x: degree[x]==0, degree.keys()))
        
        rtn = []
        while stk:
            node = stk.pop()
            rtn.append(node)
            for nei in adj[node]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    stk.append(nei)
        
        return rtn * (len(rtn) == numCourses)
            