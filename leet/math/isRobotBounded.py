class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        
        for i in instructions:
            if i == 'G':
                x += dx
                y += dy
            elif i == 'L':
                dx, dy = dy, -dx
            elif i == 'R':
                dx, dy = -dy, dx
        
        return (x,y)==(0,0) or (dx, dy) != (0, 1)
