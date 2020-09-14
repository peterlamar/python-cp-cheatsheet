"""
solved wrong problem, paths can start from anywhere
TODO: ask better questions

degree[neigh]: 3
matrix[neigh[0]][neigh[1]]: 8
matrix[node[0]][node[1]]: 4
neigh: (1, 2)
node: (0, 2)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.cnt = 0
        
        if len(matrix) == 0:
            return 0

        def dfsn(coord, prev):
            y,x = coord
            myval = matrix[y][x]
            d1 = d2 = 0
            if myval > prev:
                if y + 1 < len(matrix):
                    d1 = dfsn((y+1,x), myval) 
                if x + 1 < len(matrix[y]):
                    d2 = dfsn((y,x+1), myval) 
                return max(d1, d2) + 1 
            else:
                return 0

        def dfsp(coord, prev):
            y,x = coord
            myval = matrix[y][x]
            d1 = d2 = 0
            if myval < prev:
                if y + 1 < len(matrix):
                    d1 = dfsp((y+1,x), myval) 
                if x + 1 < len(matrix[y]):
                    d2 = dfsp((y,x+1), myval) 
                return max(d1, d2) + 1 
            else:
                return 0
        
        dn = dfsn((0,0), float('-inf'))
        dp = dfsp((0,0), float('inf'))

        
        return max(dn, dp)
    
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return 1
        
        adj = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                nei = [(y-1,x), (y+1,x), (y,x+1), (y, x-1)]
                for ny,nx in nei:
                    if 0<=ny<len(matrix) and 0<=nx<len(matrix[y]) and matrix[y][x] < matrix[ny][nx]:                        
                        adj[(y,x)].append((ny,nx))
                        degree[(ny,nx)] += 1
                        if (y,x) not in degree:
                            degree[(y,x)] = 0
        
        queue = deque(filter(lambda x: degree[x]==0, degree.keys()))

        max_path_len = 0
        while queue:
            max_path_len += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neigh in adj[node]:
                    degree[neigh] -= 1
                    if not degree[neigh]:
                        queue.append(neigh)
                
        
        return max_path_len


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        Y = len(matrix)
        X = len(matrix[0])
        dp = [[0] * X for i in range(Y)]

        def dfs(y, x):
            if dp[y][x] == 0:
                val = matrix[y][x]
                dp[y][x] = 1 + max(
                dfs(y,x-1) if x and matrix[y][x-1] < val else 0,
                dfs(y,x+1) if x+1 < X and matrix[y][x+1] < val else 0,
                dfs(y-1,x) if y and matrix[y-1][x] < val else 0,
                dfs(y+1,x) if y+1 < Y and matrix[y+1][x] < val else 0,
                )
            return dp[y][x]

        return max(dfs(y,x) for y in range(Y) for x in range(X))