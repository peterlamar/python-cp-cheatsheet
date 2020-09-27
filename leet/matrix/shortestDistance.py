class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        Y = len(grid)
        X = len(grid[0])
        
        B = 0
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == 1:
                    B += 1
        
        minDist = float('inf')
        
        for my in range(Y):
            for mx in range(X):
                visited = [[False] * X for _ in range(Y)]

                if grid[my][mx] != 0:
                    continue
                
                q = deque([(my,mx,0)])
                blds = 0
                dist = 0
                
                while q:
                    y, x, cnt = q.pop()
                    
                    if grid[y][x] == 1:
                        dist += cnt
                        blds += 1
                        if blds == B:
                            minDist = min(minDist, dist)
                            break
                        continue

                    if x > 0 and not visited[y][x-1] and grid[y][x-1] != 2:
                        visited[y][x-1] = True
                        q.appendleft((y,x-1,cnt+1))
                    if x+1 < X and not visited[y][x+1] and grid[y][x+1] != 2:
                        visited[y][x+1] = True
                        q.appendleft((y,x+1,cnt+1))
                    if y > 0 and not visited[y-1][x] and grid[y-1][x] != 2:
                        visited[y-1][x] = True
                        q.appendleft((y-1,x,cnt+1))
                    if y+1 < Y and not visited[y+1][x] and grid[y+1][x] != 2:
                        visited[y+1][x] = True
                        q.appendleft((y+1,x,cnt+1))

        return minDist if minDist != float('inf') else -1
                    
                        