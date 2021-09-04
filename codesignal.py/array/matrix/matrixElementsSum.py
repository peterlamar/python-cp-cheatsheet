"""
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

matrixElementsSum(matrix) = 9.
Read by column and add up
"""
def matrixElementsSum(matrix):
    R = len(matrix) 
    C = len(matrix[0])
    rtn = 0
    
    for c in range(C):
        for r in range(R):
            if matrix[r][c] == 0:
               break
            else:
                rtn += matrix[r][c]

    return rtn