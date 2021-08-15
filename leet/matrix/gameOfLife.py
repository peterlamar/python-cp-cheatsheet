class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0,2 - dead, dead->live
        # 1,3 - live, live->dead
        
        def neighbors(r,c):
            for nr, nc in ((r,c-1), (r,c+1),(r-1,c),(r+1,c),(r-1,c-1),
                           (r+1,c+1),(r-1,c+1),(r+1,c-1)):
                if 0<=nr<R and 0<=nc<C:
                    yield nr, nc
        
        R = len(board)
        C = len(board[0])
        
        for r in range(R):
            for c in range(C):
                cnt = 0
                
                for x,y in neighbors(r,c):
                    cnt += board[x][y] % 2
                
                if board[r][c] == 0:
                    if cnt == 3:
                        board[r][c] = 2
                else:
                    if cnt < 2 or cnt > 3:
                        board[r][c] = 3
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0
