class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i = j = 0
        m = n
        matrix = [[0 for x in range(n)] for y in range(n)]
        num = (n for n in range(1, n * n + 1))
        while i < m and j < m:
            for k in range(j, n):
                matrix[i][k] = next(num)
            i += 1
            for k in range(i, m):
                matrix[k][n - 1] = next(num)
            n -= 1
            if i < m:
                for k in range(n - 1, j - 1, -1):
                    matrix[m - 1][k] = next(num)
                m -= 1
            if j < n:
                for k in range(m - 1, i - 1, -1):
                    matrix[k][j] = next(num)
                j += 1     
        return matrix