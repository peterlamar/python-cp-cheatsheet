class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ans = 0
        
        Y = len(grid)
        X = len(grid[0])
        
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == 1:
                    ans += 4
                
                    if x > 0 and grid[y][x-1] == 1:
                        ans -= 2

                    if y > 0 and grid[y-1][x] == 1:
                        ans -= 2
        
        return ans