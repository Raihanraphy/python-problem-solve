class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        columns = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in list(rows):
            for j in range(n):
                matrix[i][j] = 0
        for i in list(columns):
            for j in range(m):
                matrix[j][i] = 0
