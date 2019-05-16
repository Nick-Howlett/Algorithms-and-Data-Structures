class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        if obstacleGrid[0][0] or obstacleGrid[n - 1][m - 1]:
            return 0
        memo = [[0 for x in range(m)] for y in range(n)]
        start = 0
        memo[start][start] = 1
        for i in range(n):
            for j in range(m):
                if not i and not j:
                    continue
                top = left = 0
                if i > 0:
                    top = 0 if obstacleGrid[i - 1][j] else memo[i - 1][j]
                if j > 0:
                    left = 0 if obstacleGrid[i][j - 1] else memo[i][j - 1]
                memo[i][j] = top + left
        return memo[n - 1][m - 1]