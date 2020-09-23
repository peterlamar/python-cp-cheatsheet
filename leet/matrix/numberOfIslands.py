class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        Y = len(grid)
        if Y == 0:
            return 0
        
        X = len(grid[0])
        
        def dfs(y,x):
            if y < 0 or x < 0 or y > Y-1 or x > X-1:
                return
            
            if grid[y][x] == "1":
                grid[y][x] = "0"
                dfs(y+1,x)
                dfs(y,x+1)
                dfs(y-1,x)
                dfs(y,x-1)

        
        ans = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    dfs(y,x)
                    ans += 1
        
        return ans
        
            
            