class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r,c-1), (r,c+1), (r-1, c), (r+1,c)):
                if 0<=nr<R and 0<=nc<C:
                    yield nr, nc
        
        
        def dfs(r,c, index):
            area = 0
            grid[r][c] = index
            for x,y in neighbors(r,c):
                if grid[x][y] == 1:
                    area += dfs(x,y, index)
            return area + 1
        
        index = 2
        areas = {}
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    areas[index] = dfs(r, c, index)
                    index += 1
        
        rtn = max(areas.values() or [0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    possible = set(grid[i][j] for i, j in neighbors(r,c) if grid[i][j] > 1)
                    rtn = max(rtn, sum(areas[k] for k in possible)+1)
        
        return rtn

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        def neighbors(r, c):
            for x,y in ((r,c-1),(r,c+1),(r-1,c),(r+1,c)):
                if 0<=x<N and 0<=y<N:
                    yield x,y
        
        def dfs(r,c,index):
            area = 0
            grid[r][c] = index
            for x,y in neighbors(r,c):
                if grid[x][y] == 1:
                    area += dfs(x,y,index)
            return area+1
        
        # Paint all islands an index number
        areas = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    areas[index] = dfs(r,c, index)
                    index += 1
        
        rtn = max(areas.values() or [0])
        
        # Go through 0's and count potential areas
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    possible = set(grid[i][j] for i,j in neighbors(r,c) if grid[i][j] > 1)
                    rtn = max(rtn, sum(areas[p] for p in possible)+1)
        
        return rtn


    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        paint each island, store its area
        go through 0's, count neighbors area and return largest
        """
        
        def neighbors(r,c):
            for x,y in ((r+1,c),(r-1,c),(r,c-1),(r,c+1)):
                if 0<=x<N and 0<=y<N:
                    yield x,y
        
        def paint(r, c, pnum):
            grid[r][c] = pnum
            area = 0
            for x, y in neighbors(r,c):
                if grid[x][y] == 1:
                    area += paint(x,y, pnum) 
            return area + 1
                
        
        N = len(grid)
        areas = dict()
        pnum = 2
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    areas[pnum] = paint(r,c, pnum)
                    pnum += 1
        

        maxSum = max(areas.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    tmpSum = 1
                    possible = set()
                    for x,y in neighbors(r,c):
                        if grid[x][y] != 0:
                            possible.add(grid[x][y])
                    for p in possible:
                        tmpSum += areas[p]
                    maxSum = max(maxSum, tmpSum)

        return maxSum
        
        