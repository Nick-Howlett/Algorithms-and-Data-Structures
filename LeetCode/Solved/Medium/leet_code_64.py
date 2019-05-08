class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      memo = [[sys.maxsize for x in range(len(grid[0]))] for y in range(len(grid))]
      memo[0][0] = grid[0][0]
      for i in range(len(grid)):
          for j in range(len(grid[0])):
            if i == 0 and j == 0:
              continue
            x = i if i == 0 else i - 1
            y = j if j == 0 else j - 1
            memo[i][j] = min(memo[i][y], memo[x][j]) + grid[i][j]
      return memo[len(grid) - 1][len(grid[0]) - 1]
                