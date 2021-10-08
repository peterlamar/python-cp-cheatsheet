"""
For cell = "a1", the output should be
chessKnight(cell) = 2.
For cell = "c2", the output should be
chessKnight(cell) = 6.
"""
def chessKnight(cell):
    r = ord(cell[0]) - ord('a') 
    c = int(cell[1])
    
    def neighbors(r, c):
        for nr, nc in ((r+1,c-2), (r+1,c+2), (r-1,c-2), (r-1,c+2), (r+2, c-1), (r+2,c+1), (r-2, c-1), (r-2,c+1)):
            if 0<=nr<8 and 0<nc<=8:
                yield nr, nc
                
    rtn = 0
    for nr, nc in neighbors(r, c):
        rtn += 1
    
    return rtn
