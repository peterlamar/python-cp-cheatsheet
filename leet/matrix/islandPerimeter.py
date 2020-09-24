"""
time: O(YX)
space: 1
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        
        Y = len(grid)
        X = len(grid[0])
        
        ans = 0
        
        for y in range(Y):
            for x in range(X):
                if grid[y][x]:
                    ans += 4
                    
                    if y > 0 and grid[y-1][x]:
                        ans -= 2
                    if x > 0 and grid[y][x-1]:
                        ans -= 2
        
        return ans
            