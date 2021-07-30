"""
time: X * Y
space: worst case X * Y
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        Y = len(grid)
        X = len(grid[0])
        
        def dfs(y, x):
            if y < 0 or x < 0 or y > Y-1 or x > X-1:
                return
            if grid[y][x] == "1":
                grid[y][x] = "0"
                dfs(y, x-1)
                dfs(y, x+1)
                dfs(y-1, x)
                dfs(y+1, x)
                
        ans = 0
        
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == "1":
                    dfs(y, x)
                    ans += 1
        
        return ans

    def numIslands(self, grid : List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            
            if grid[r][c] == '1':
                grid[r][c] = '0'
            
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        
        rtn = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    rtn += 1
                    dfs(r,c)
        
        return rtn
        