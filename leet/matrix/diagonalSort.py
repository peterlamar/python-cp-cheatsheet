class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, d = len(mat), len(mat[0]), defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[j - i].append(mat[i][j])
                
        for k in d:
            for i, num in enumerate(sorted(d[k])):
                mat[i + max(-k, 0)][k + i + max(-k, 0)] = num
                
        return mat