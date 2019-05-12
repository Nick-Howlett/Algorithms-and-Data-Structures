class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for j in range(n)]
        solns = self.dfs(board, 0, n)
        for soln in solns:
            for i in range(n):
                soln[i] = "".join(soln[i])
        return solns
    
    
    def valid(self, board, row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True
            
    
    def dfs(self, board, row, n):
        if row == n:
            return [[row[:] for row in board]]
        solns = []
        for col in range(n):
            if self.valid(board, row, col):
                board[row][col] = "Q"
                solns.extend(self.dfs(board, row + 1, n))
            board[row][col] = "."
        return solns