"""

1, 3, 1
1, 5, 1
4, 2, 1

1, 4, 5
2, 7, 6
6, 8, 7


1, 4, 5
2, 7, 6
6, 8, 7

"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # Row
        n = len(grid[0]) # Column
        for x in range(0, m):
            for y in range(0,n):
                if x == 0 and y == 0:
                    continue
                if x == 0:
                    grid[x][y] += grid[x][y-1]
                elif y == 0:
                    grid[x][y] += grid[x-1][y]
                else:
                    grid[x][y] += min(grid[x-1][y],grid[x][y-1])

        return grid[-1][-1]