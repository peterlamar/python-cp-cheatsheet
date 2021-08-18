class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        rr = rc = 0
        rtn = 0
        
        # Find Rook
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rr = r
                    rc = c
        
        for i in range(rc-1, -1, -1):
            if board[rr][i] == 'B':
                break
            elif board[rr][i] == 'p':
                rtn += 1
                break
        
        for i in range(rc+1, 8):
            if board[rr][i] == 'B':
                break
            elif board[rr][i] == 'p':
                rtn += 1
                break
        
        for i in range(rr-1, -1, -1):
            if board[i][rc] == 'B':
                break
            elif board[i][rc] == 'p':
                rtn += 1
                break

        for i in range(rr+1, 8):
            if board[i][rc] == 'B':
                break
            elif board[i][rc] == 'p':
                rtn += 1
                break
                
        return rtn