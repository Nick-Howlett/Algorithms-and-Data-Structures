class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      memo = [[None for x in range(m)] for y in range(n)]
      memo[0][0] = 1
      for i in range(1, m):
        memo[0][i] = 1
      for i in range(1, n):
        memo[i][0] = 1
      for i in range(1, n):
        for j in range(1, m):
          memo[i][j] = memo[i][j - 1] + memo[i - 1][j]
      return memo[n - 1][m - 1]