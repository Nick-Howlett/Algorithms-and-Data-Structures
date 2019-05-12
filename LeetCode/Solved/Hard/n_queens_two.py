class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0 for i in range(n)] for j in range(n)]
        return self.dfs(board, 0, n)
            
    def valid(self, board, row, col):
        for i in range(row):
            if board[i][col]:
                return False
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j]:
                return False
            i -= 1
            j += 1
        return True
    
    def dfs(self, board, row, n):
        if row == n:
            return 1
        total = 0
        for col in range(n):
            if self.valid(board, row, col):
                board[row][col] = 1
                total += self.dfs(board, row + 1, n)
                board[row][col] = 0
        return total