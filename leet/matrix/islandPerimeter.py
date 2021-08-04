"""
time: O(YX)
space: 1
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rtn = 0
        
        # check up and left 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    rtn += 4
                    if r > 0 and grid[r-1][c]:
                        rtn -= 2
                    if c > 0 and grid[r][c-1]:
                        rtn -= 2
        
        return rtn
            