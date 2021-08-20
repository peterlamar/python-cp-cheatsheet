class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)
        
        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue
                
                num = board[r][c]
                
                if num in rows[r]:
                    return False
                rows[r].add(num)

                if num in cols[c]:
                    return False
                cols[c].add(num)
                
                # Divide board into indexes
                boxIdx = (r // 3) * 3 + c // 3
                if num in box[boxIdx]:
                    return False
                box[boxIdx].add(num)
                
        return True