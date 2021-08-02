class Solution:
        def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def neighbors(r,c):
            for x,y in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=x<R and 0<=y<C:
                    yield x,y
        
        def dfs(r,c):
            area = 0
            grid[r][c] = 0
            for x,y in neighbors(r,c):
                if grid[x][y] == 1:
                    area += dfs(x,y)
            return area + 1
            
        
        if not grid:
            return
        
        R = len(grid)
        C = len(grid[0])
        
        mxArea = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    mxArea = max(mxArea, dfs(r,c))
        
        return mxArea
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        Y = len(grid)
        if Y == 0:
            return 0
        
        X = len(grid[0])
        
        def dfs(y,x):
            if y < 0 or x < 0 or y > Y-1 or x > X-1:
                return 0
            
            if grid[y][x] == 1:
                grid[y][x] = 0
                return dfs(y+1,x) + dfs(y,x+1) + dfs(y-1,x) + dfs(y,x-1) + 1

            return 0
        
        ans = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    cnt = dfs(y,x)
                    ans = max(ans, cnt)
        
        return ans