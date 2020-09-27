class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([(0,0,0)])
        visited = set()
        moves = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))

        while q:
            px, py, cnt = q.pop()
            
            if px == abs(x) and py == abs(y):
                return cnt 
            
            for dx, dy in moves:
                px1 = px+dx
                py1 = py+dy
                if (px1,py1) not in visited and px1 >= -2 and py1 >= -2:
                    q.appendleft((px1, py1,cnt+1))
                    visited.add((px1, py1))

        return -1


    def minKnightMoves1(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        res = 0
        while x > 4 or y > 4:
            res += 1
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                x -= 1 if x >= 1 else -1
                y -= 2 
                
        q = deque([(0,0,0)])
        visited = set()
        moves = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))

        while q:
            px, py, cnt = q.pop()
            
            if px == abs(x) and py == abs(y):
                return cnt + res
            
            for dx, dy in moves:
                px1 = px+dx
                py1 = py+dy
                if (px1,py1) not in visited and px1 >= -2 and py1 >= -2:
                    q.appendleft((px1, py1,cnt+1))
                    visited.add((px1, py1))

        return -1