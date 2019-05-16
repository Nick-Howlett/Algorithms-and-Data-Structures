class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        i = j = 0
        m, n = len(matrix), len(matrix[0])
        ret = []
        while i < m and j < n:
            for k in range(j, n):
                ret.append(matrix[i][k])
            i += 1
            for k in range(i, m):
                ret.append(matrix[k][n - 1])
            n -= 1
            if i < m:
                for k in range(n - 1, j - 1, -1):
                    ret.append(matrix[m - 1][k])
                m -= 1
            if j < n:
                for k in range(m - 1, i - 1, -1):
                    ret.append(matrix[k][j])
                j += 1
        return ret