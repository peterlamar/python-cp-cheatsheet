class Solution:
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