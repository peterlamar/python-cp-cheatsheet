class Solution:
    def dot(self, row, col):
        R = len(row)
        C = len(col)
        r = c = ans = 0
        while r < R and c < C:
            index_row, val_row = row[r]
            index_col, val_col = col[c]
            if index_row < index_col:
                r += 1
            elif index_row > index_col:
                c += 1
            else:
                ans += val_row * val_col
                r += 1
                c += 1
        return ans
        
    
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return
        
        Ay = len(A)
        Ax = len(A[0])
        By = len(B)
        Bx = len(B[0])
        
        rowVec = [
            [
                (x, A[y][x]) for x in range(Ax) if A[y][x] 
            ]
            for y in range(Ay)
        ]
        
        colVec = [
            [
                (y, B[y][x]) for y in range(By) if B[y][x] 
            ]
            for x in range(Bx)
        ]
        
        ans = [
            [
                self.dot(row, col)
                for col in colVec
            ] for row in rowVec
        ]
        
        return ans