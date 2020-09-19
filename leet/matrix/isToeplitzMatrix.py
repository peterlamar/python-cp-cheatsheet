class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 0: return True
        if len(matrix) == 1 and len(matrix[0]) == 0: return true
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        
        return True