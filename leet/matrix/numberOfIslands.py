"""
time: X * Y
space: worst case X * Y
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        def neighbors(r,c):
            for nr, nc in ((r, c-1), (r, c+1), (r-1, c), (r+1, c)):
                if 0<=nr<R and 0<=nc<C:
                    yield nr, nc
                    
        def dfs(r, c):
            grid[r][c] = '0'
            for x,y in neighbors(r,c):
                if grid[x][y] == '1':
                    dfs(x,y)
        
        rtn = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':                
                    dfs(r, c)
                    rtn += 1
        
        return rtn
        